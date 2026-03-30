#!/bin/zsh
JAVA=/opt/homebrew/Cellar/openjdk/24.0.1/libexec/openjdk.jdk/Contents/Home/bin
JAVAC=$JAVA/javac
JAVA_BIN=$JAVA/java
RESOURCES=src/main/resources

echo "🛑 Oude server stoppen (poort 8090)..."
lsof -ti tcp:8090 | xargs kill -9 2>/dev/null && echo "   Gestopt." || echo "   Niets te stoppen."
sleep 1

echo "🎨 SCSS eenmalig compileren..."
sass $RESOURCES/styles.scss $RESOURCES/styles.css --no-source-map
sass $RESOURCES/placeholder.scss $RESOURCES/placeholder.css --no-source-map

echo "👀 SCSS watcher starten (achtergrond)..."
sass --watch $RESOURCES/styles.scss:$RESOURCES/styles.css --watch $RESOURCES/placeholder.scss:$RESOURCES/placeholder.css --no-source-map &
SASS_PID=$!

echo "🔨 Java compileren..."
mkdir -p target/classes
$JAVAC -d target/classes src/main/java/org/example/Main.java
if [ $? -ne 0 ]; then
  echo "❌ Compilatie mislukt — server niet gestart."
  kill $SASS_PID 2>/dev/null
  exit 1
fi

echo ""
echo "🚀 Server draait op http://localhost:8090"
echo "   ✏️  HTML/CSS wijzigingen → alleen browser refreshen (F5)"
echo "   🎨  SCSS wijzigingen    → automatisch gecompileerd + browser refreshen"
echo "   ☕  Java wijzigingen    → herstart run.sh"
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
trap "kill $SASS_PID 2>/dev/null" EXIT
$JAVA_BIN -cp "$SCRIPT_DIR/$RESOURCES:$SCRIPT_DIR/target/classes" org.example.Main
