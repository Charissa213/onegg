package org.example;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class Main {

    public static void main(String[] args) throws IOException {
        int port = 8090;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", new StaticFileHandler());
        server.start();
        System.out.println("✅ Onegg website draait op http://localhost:" + port);
    }

    static class StaticFileHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/") || path.equals("/index.html")) {
                path = "/index.html";
            }

            InputStream is = Main.class.getResourceAsStream(path);
            if (is == null) {
                String response = "404 Not Found";
                exchange.sendResponseHeaders(404, response.getBytes().length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(response.getBytes());
                }
                return;
            }

            String contentType = getContentType(path);
            byte[] bytes = is.readAllBytes();
            long totalLength = bytes.length;

            // Cache-Control: HTML en CSS/JS nooit cachen (dev), rest 1 uur
            if (contentType.startsWith("text/html") || contentType.startsWith("text/css") || contentType.startsWith("application/javascript")) {
                exchange.getResponseHeaders().set("Cache-Control", "no-cache, no-store, must-revalidate");
            } else {
                exchange.getResponseHeaders().set("Cache-Control", "public, max-age=3600");
            }

            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.getResponseHeaders().set("Accept-Ranges", "bytes");

            // Range-request support (voor video streaming)
            String rangeHeader = exchange.getRequestHeaders().getFirst("Range");
            if (rangeHeader != null && rangeHeader.startsWith("bytes=")) {
                String[] parts = rangeHeader.substring(6).split("-");
                long start = Long.parseLong(parts[0]);
                long end = (parts.length > 1 && !parts[1].isEmpty())
                        ? Long.parseLong(parts[1])
                        : totalLength - 1;
                end = Math.min(end, totalLength - 1);
                long chunkLength = end - start + 1;

                exchange.getResponseHeaders().set("Content-Range",
                        "bytes " + start + "-" + end + "/" + totalLength);
                exchange.sendResponseHeaders(206, chunkLength);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(bytes, (int) start, (int) chunkLength);
                }
            } else {
                exchange.sendResponseHeaders(200, totalLength);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(bytes);
                }
            }
        }

        private String getContentType(String path) {
            String p = path.toLowerCase();
            if (p.endsWith(".html"))  return "text/html; charset=UTF-8";
            if (p.endsWith(".css"))   return "text/css; charset=UTF-8";
            if (p.endsWith(".js"))    return "application/javascript";
            if (p.endsWith(".png"))   return "image/png";
            if (p.endsWith(".jpg") || p.endsWith(".jpeg")) return "image/jpeg";
            if (p.endsWith(".gif"))   return "image/gif";
            if (p.endsWith(".svg"))   return "image/svg+xml";
            if (p.endsWith(".webp"))  return "image/webp";
            if (p.endsWith(".ico"))   return "image/x-icon";
            if (p.endsWith(".mp4"))   return "video/mp4";
            if (p.endsWith(".webm"))  return "video/webm";
            if (p.endsWith(".ogg"))   return "video/ogg";
            if (p.endsWith(".mov"))   return "video/quicktime";
            if (p.endsWith(".woff"))  return "font/woff";
            if (p.endsWith(".woff2")) return "font/woff2";
            if (p.endsWith(".ttf"))   return "font/ttf";
            if (p.endsWith(".otf"))   return "font/otf";
            return "application/octet-stream";
        }
    }
}
