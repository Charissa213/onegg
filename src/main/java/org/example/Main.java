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
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(200, bytes.length);
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(bytes);
            }
        }

        private String getContentType(String path) {
            String p = path.toLowerCase();
            if (p.endsWith(".html"))        return "text/html; charset=UTF-8";
            if (p.endsWith(".css"))         return "text/css; charset=UTF-8";
            if (p.endsWith(".js"))          return "application/javascript";
            // Afbeeldingen
            if (p.endsWith(".png"))         return "image/png";
            if (p.endsWith(".jpg") ||
                p.endsWith(".jpeg"))        return "image/jpeg";
            if (p.endsWith(".gif"))         return "image/gif";
            if (p.endsWith(".svg"))         return "image/svg+xml";
            if (p.endsWith(".webp"))        return "image/webp";
            if (p.endsWith(".ico"))         return "image/x-icon";
            // Video's
            if (p.endsWith(".mp4"))         return "video/mp4";
            if (p.endsWith(".webm"))        return "video/webm";
            if (p.endsWith(".ogg"))         return "video/ogg";
            if (p.endsWith(".mov"))         return "video/quicktime";
            // Fonts
            if (p.endsWith(".woff"))        return "font/woff";
            if (p.endsWith(".woff2"))       return "font/woff2";
            if (p.endsWith(".ttf"))         return "font/ttf";
            if (p.endsWith(".otf"))         return "font/otf";
            return "application/octet-stream";
        }
    }
}

