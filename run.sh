#!/bin/zsh
JAVA_HOME=$(/usr/libexec/java_home 2>/dev/null || echo "/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home")
JAVAC=$JAVA_HOME/bin/javac
JAVA_BIN=$JAVA_HOME/bin/java
RESOURCES=src/main/resources

echo "🛑 Oude server stoppen (poort 8090)..."
lsof -ti tcp:8090 | xargs kill -9 2>/dev/null && echo "   Gestopt." || echo "   Niets te stoppen."
sleep 1

echo "🎨 SCSS eenmalig compileren..."
sass $RESOURCES/styles.scss $RESOURCES/styles.css --no-source-map
sass $RESOURCES/korg-minilogue.scss $RESOURCES/korg-minilogue.css --no-source-map
sass $RESOURCES/media.scss $RESOURCES/media.css --no-source-map
sass $RESOURCES/tour.scss $RESOURCES/tour.css --no-source-map
if [ $? -ne 0 ]; then
  echo "❌ SCSS compilatie mislukt."
  exit 1
fi

echo "👀 SCSS watcher starten (achtergrond)..."
sass --watch $RESOURCES/styles.scss:$RESOURCES/styles.css $RESOURCES/korg-minilogue.scss:$RESOURCES/korg-minilogue.css $RESOURCES/media.scss:$RESOURCES/media.css $RESOURCES/tour.scss:$RESOURCES/tour.css --no-source-map &
SASS_PID=$!
trap "kill $SASS_PID 2>/dev/null" EXIT

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
$JAVA_BIN -cp "$SCRIPT_DIR/$RESOURCES:$SCRIPT_DIR/target/classes" org.example.Main
