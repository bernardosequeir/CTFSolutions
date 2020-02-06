import java.io.PrintStream;
import java.util.Arrays;
import java.util.Base64;

public class problem {
    public static String get_flag() {
        String string = "Hint: Don't worry about the schematics";
        String string2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
        String string3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
        byte[] arrby = string2.getBytes();
        byte[] arrby2 = string3.getBytes();
        byte[] arrby3 = new byte[arrby2.length];
        for (int i = 0; i < arrby2.length; ++i) {
            arrby3[i] = arrby2[arrby[i] - 90];
        }
        System.out.println(Arrays.toString(Base64.getDecoder().decode(arrby3)));
        return new String(Base64.getDecoder().decode(arrby3));
    }

    public static void main(String[] arrstring) {
	String flag = get_flag();
        System.out.println(flag);
    }
}
