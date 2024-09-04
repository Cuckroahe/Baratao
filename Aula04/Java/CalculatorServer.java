import java.rmi.Naming;

public class CalculatorServer{
    public static void main(String[] args) {
        CalculatorImpl calc = new CalculatorImpl();
        Naming.rebind("rmi://localhost:1099/CalculatorService", calc);
        System.out.println("sevidor aguardando...");
    } catch(Exception e){
    e.printStackTrace();
}}