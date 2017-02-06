int PAN1 = 0;       // USE THIS VALUE TO SET THE FIRST ANGLE OF THE PAN
int PAN2 = 0;       // USE THIS VALUE TO SET THE SECOND ANGLE OF THE PAN
int TILT1 = 0;      // USE THIS VALUE TO SET THE FIRST ANGLE OF THE TILT
int TILT2 = 0;      // USE THIS VALUE TO SET THE SECOND ANGLE OF THE TILT


void setup() {

  Serial.begin(9600);
  pinMode (11,OUTPUT); 
  // put your setup code here, to run once:

}

void loop() 
{

  while(Serial.available()>0){
    char a = Serial.read();
    if (a == 'A'){
      //while(Serial.available())
      digitalWrite(11,HIGH);
      delay(450);
      String b = "" ;
       
       while(Serial.available()>0)
       {
        char d = Serial.read();
        b+= d;
        PAN1 = b.toInt();
        //if (PAN1 == 12)         // THIS IS FOR TEST PURPOSES ONLY
        //digitalWrite(11,LOW);   // THIS IS FOR TEST PURPOSES ONLY
      }
        
     }
     
     if (a == 'B')
     {
      //while(Serial.available())
      digitalWrite(11,HIGH);
      delay(450);
      String b = "" ;
       
       while(Serial.available()>0)
       {
        char d = Serial.read();
        b+= d;
        PAN2 = b.toInt();
        //if (PAN2 == 22)       // THIS IS FOR TEST PURPOSES ONLY
        //digitalWrite(11,LOW); // THIS IS FOR TEST PURPOSES ONLY
       }   
     }

     if (a == 'C')
     {
      //while(Serial.available())
      digitalWrite(11,HIGH);
      delay(450);
      String b = "" ;
       
       while(Serial.available()>0)
       {
        char d = Serial.read();
        b+= d;
        TILT1 = b.toInt();
        //if (TILT1 == 44)        // THIS IS FOR TEST PURPOSES ONLY
        //digitalWrite(11,LOW);   // THIS IS FOR TEST PURPOSES ONLY
       }   
     }

     
     if (a == 'D')
     {
      //while(Serial.available())
      digitalWrite(11,HIGH);
      delay(450);
      String b = "" ;
       
       while(Serial.available()>0)
       {
        char d = Serial.read();
        b+= d;
        TILT2 = b.toInt();        
        //if (TILT2 == 180)       // THIS IS FOR TEST PURPOSES ONLY
        //digitalWrite(11,LOW);   // THIS IS FOR TEST PURPOSES ONLY
       }   
     }
   }
 }
            
 
  
  // put your main code here, to run repeatedly:


