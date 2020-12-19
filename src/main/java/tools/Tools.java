package tools;

import java.util.Collections;

public class Tools {
    public static void show_subtitle(String message) {
        // 输出运行模块的子标题
        System.out.println(
                String.join("", Collections.nCopies(15, "-")) + '>'
                        + message
                        + '<' + String.join("", Collections.nCopies(15, "-")));
    }

    public static void show_title(String message) {
        // 输出运行模块的子标题
        System.out.println(
                String.join("", Collections.nCopies(15, "=")) + '>'
                        + message
                        + '<' + String.join("", Collections.nCopies(15, "=")));
    }
}
