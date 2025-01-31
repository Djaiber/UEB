import java.util.Scanner;

public class fibonacciCiclico {
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Cual numero desea calcular de la Serie de Fibonacci: ");
    int n = scanner.nextInt();
    scanner.close();
    
    int resultado = fibonacciCiclico(n);
    System.out.println("El numero " + n + " de la Serie de Fibonacci es: " + resultado);
}

public static int fibonacciCiclico(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    int Num1 = 0, Num2 = 1;
    for (int i = 2; i <= n; i++) {
        int Siguiente = Num1 + Num2;
        Num1 = Num2;
        Num2 = Siguiente;
    }
    return Num2;
}
}