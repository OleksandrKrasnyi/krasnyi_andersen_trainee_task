import java.util.Scanner;
import java.util.InputMismatchException;

public class One {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		try {
		
		System.out.println("Введите число: ");
		int number = scanner.nextInt();
		scanner.nextLine();
		
		if (number > 7) {
			System.out.println("Привет");
		}}
		catch (InputMismatchException e) {
			System.out.println("Неверный тип вводных данных, "
							+ "должно быть целое число.");
		}
		finally {
			scanner.close();
		}
	}
}
