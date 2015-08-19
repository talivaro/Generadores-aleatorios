package genaleatorios;

import javax.swing.JOptionPane;

/**
 *
 * @author Talivaro
 */
public class GenAleatorios {

    
    public void midsquare(){
         String num= JOptionPane.showInputDialog(null,"Ingrese el valor de la semilla");
         int xo=Integer.parseInt(num);
        
        int n=num.length()/2;
        
        if(num.length()%2 == 0){
            
            String repe= JOptionPane.showInputDialog(null,"Numero de repeticiones");
            int repe2=Integer.parseInt(repe);
            for(int i=0;i<repe2 ;i++){
                String aux="";
                String punto="";
                int xo2=xo*xo;
                String s=Integer.toString(xo2);
             
                    for(int j=0;j<(4*n)-s.length();j++){
                        aux += "0";   
                    }
                
                s=aux+s;
                System.out.println(s);
                String s2=s.substring((2*num.length())/4,(2*num.length()*3)/4);
                System.out.println("x"+(i+1)+": "+s2);
                punto ="0."+s2;   
                System.out.println("U"+(i+1)+": "+punto);
                int salida=Integer.parseInt(s2);
              
                xo=salida;
        }
        } else{
            JOptionPane.showInputDialog(null,"Las cifras son impares");
        }
    }
   
    public void CongMixto(){
        
        String num=JOptionPane.showInputDialog(null,"Ingrese Xo:");
              int xo=Integer.parseInt(num);
              String rep=JOptionPane.showInputDialog(null,"Numero de valores:");
              int repe=Integer.parseInt(rep);
              
              int xn=0,a=5,b=3,m=16;
              for(int i=0; i<repe;i++){
               int mod;
                        
               xn=a*xo+b;
               //System.out.println(xn);
               mod=xn%m;
               System.out.println("X"+(i+1)+": "+mod);
               float ui=mod/m;
               System.out.println("U"+(i+1)+": "+ui);
               xo=mod;
              }
    }
    
    public void CongCombi(){
        String num=JOptionPane.showInputDialog(null,"Ingrese Xo:");
              double xo1=Double.parseDouble(num);
        String num2=JOptionPane.showInputDialog(null,"Ingrese Yo:");
              double xo2=Double.parseDouble(num2);
        String num3=JOptionPane.showInputDialog(null,"Ingrese zo:");
              double xo3=Double.parseDouble(num3);
        String rep=JOptionPane.showInputDialog(null,"Numero de valores");
              int repe=Integer.parseInt(rep);
              double xn1,xn2,xn3;
        
         for(int i=0; i<repe;i++){
             xn1= (171*xo1)%30269;
             xn2= (172*xo2)%30307;
             xn3= (173*xo3)%30323;
//             System.out.println(xn1);
//             System.out.println(xn2);
//             System.out.println(xn3);
             double ui=(xn1/30269+(xn2/30307)+(xn3/30323))%1;
             System.out.println(ui);
             xo1=xn1;
             xo2=xn2;
             xo3=xn3;
         }
       
    }
    public static void main(String[] args) {
        // TODO code application logic here
       
        GenAleatorios g=new GenAleatorios();
       g.midsquare();
          //g.CongMixto();
       //g.CongCombi();
        
        
      
       
    }
    
}
