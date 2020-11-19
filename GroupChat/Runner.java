
package project;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.awt.FlowLayout;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.net.Socket;
import javax.swing.*; 

public class Runner {
	public static Socket client;
	public static DataInputStream dis;
	
	public static class ListenForMessage implements Runnable {

		public void run() {
			try {
				dis = new DataInputStream(client.getInputStream());
			} catch (IOException e1) {
				e1.printStackTrace();
				System.out.println(e1.getMessage());
			}
			while (true) {
				try {
					if (dis.available()!=0) {
						byte[] b = new byte[dis.available()];
						dis.readFully(b,0,dis.available());
						String backToString = new String(b);
						System.out.println(backToString);
					}
				} catch (IOException e) {
					e.printStackTrace();
				}
			}

		}
	}
	
	public static void main(String[] args) throws IOException {
		Scanner console = new Scanner(System.in);
		client = new Socket("10.42.15.189", 36310);
		System.out.println("connected");
		DataInputStream dis = new DataInputStream(client.getInputStream());
		
		System.out.println(dis.readUTF());
//		JFrame f=new JFrame();
//		 f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
//	        // Add a layout manager so that the button is not placed on top of the label
//	        f.setLayout(new FlowLayout());
//	        // Add a label and a button
//	        
//	        f.add(new JLabel(dis.readUTF()));
//	        
//	        // Arrange the components inside the window
//	        f.pack();
//	        // By default, the window is not visible. Make it visible.
//	        f.setVisible(true);
//	        String temp = dis.readUTF();
//	        while(true){
//	        	if(!(temp .equals( dis.readUTF()))){
//	        		//f.add(new JLabel(dis.readUTF()));
//	        		temp = temp + dis.readUTF();
//	        		System.out.println(temp);
	        		//f.setVisible(true);
	        	//}
	       // }
		}
		
	
	public static String importLastLine(String fileName) throws FileNotFoundException{
		Scanner texts = new Scanner (new File(fileName));
		String lastLine = "";
		while (texts.hasNext()){
			lastLine = texts.nextLine();
		}
		texts.close();
		return lastLine;
	}

public static void uploadMessage(String message, String fileName) throws IOException{
	Writer output;
output = new BufferedWriter(new FileWriter(fileName, true));  
output.append("\n" + message);
output.close();

}
public static int countLines(String fileName) throws FileNotFoundException {
	int lines = 0;
	Scanner in = new Scanner(new File(fileName));
	while (in.hasNextLine()) {
		in.nextLine();
		lines++;
	}
	in.close();
	return lines;
}

}	
