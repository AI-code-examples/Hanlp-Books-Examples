package tools;

import java.util.Collections;

public class Tools {
    /**
     * 输出运行模块的子标题
     *
     * @param message 标题的内容
     */
    public static void show_subtitle(String message) {
        System.out.println(
                String.join("", Collections.nCopies(15, "-")) + '>'
                        + message
                        + '<' + String.join("", Collections.nCopies(15, "-")));
    }

    /**
     * 输出运行模块的标题
     *
     * @param message 标题的内容
     */
    public static void show_title(String message) {
        System.out.println(
                String.join("", Collections.nCopies(15, "=")) + '>'
                        + message
                        + '<' + String.join("", Collections.nCopies(15, "=")));
    }


    /**
     * 获取项目路径
     *
     * @return 返回当前项目的绝对路径
     */
    public static String get_root_path() {
        return System.getProperty("user.dir")+"/";
    }

    public static String get_data_path() {
        return get_root_path() + "data/";
    }

    public static String icwb2_data_path() {
        return test_data_path()+"icwb2-data/";
    }

    public static String test_data_path() {
        return get_root_path() + "data/test/";
    }
}
