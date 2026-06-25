// Level 2: build "Hello, World!" from ASCII codes (no string literal)
public class HelloAscii {
    public static void main(String[] args) {
        int[] codes = { 72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33 };
        StringBuilder sb = new StringBuilder();
        for (int c : codes) {
            sb.append((char) c);
        }
        System.out.println(sb.toString());
    }
}
