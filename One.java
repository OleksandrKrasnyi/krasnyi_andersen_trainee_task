import java.util.Scanner;
import java.util.InputMismatchException;

public class One {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		try {
		
		System.out.println("������� �����: ");
		double number = scanner.nextDouble();
		scanner.nextLine();
		
		if (number > 7) {
			System.out.println("������");
		}}
		catch (InputMismatchException e) {
			System.out.println("�������� ��� ������� ������, "
							+ "������ ���� ����� �����.");
		}
		finally {
			scanner.close();
		}
	}
}
