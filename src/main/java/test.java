public class test {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        System.out.println("你好，中国!");
        System.out.println(test.class.getResource("/").getPath());
        System.out.println(test.class.getClassLoader().getResource("").getPath());
        System.out.println(System.getProperty("user.dir"));
        System.out.println(System.getProperty("user.home"));
    }

}
