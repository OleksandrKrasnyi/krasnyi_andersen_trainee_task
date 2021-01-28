import java.util.Scanner;

public class Two {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Введите имя (регистр не важен): ");
		String name = scanner.nextLine();
		scanner.close();
		name = name.substring(0,1).toUpperCase() + 
			   name.substring(1).toLowerCase();
				
		if (!name.equals("Вячеслав")) {
			System.out.println("Нет такого имени");
		} else {
			System.out.println("Привет, " + name);
		}
	}
}
