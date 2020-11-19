package project;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

public class IDK extends JFrame {
	private JPanel jContentPane = null;

	

	public IDK() {

		super();

		initialize();

    }



    private void initialize() {

        this.setSize(300, 200);

        this.setContentPane(getJContentPane());

        this.setTitle("JFrame");

    }



    private JPanel getJContentPane() {

        if (jContentPane == null) {

            jContentPane = new JPanel();

            jContentPane.setLayout(null);



            JPanel panel = new JPanel();



            panel.setBounds(61, 11, 81, 140);

            panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

            jContentPane.add(panel);



            JButton button = new JButton();
             boolean pressed = false;
            panel.add(button);
            
          //  button.setAction(panel.add(new JLabel("true")));
            
         //   if(panel.JButton)

        }

        return jContentPane;

    }
    
    

    

    public static void main(String[] args) {

        IDK frame = new IDK();

        frame.setVisible(true);
        
        
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

    }
}
