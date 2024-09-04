import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class CalculatorImpl  extends UnicastRemoteObject implements Calculator{

    protected CalculatorImpl() throws RemoteException{
        super();
    }

    public int add(int x, int y){
        return x + y;
    }
}