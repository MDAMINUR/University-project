int irPin1=7;
int irPin2=8;
int count=0;
int mod=0;
int divs=0;
boolean state1 = true;
boolean state2 = true;
boolean insideState = false;
boolean outsideIr=false;
boolean isPeopleExiting=false;
int i=1;
void setup() {
Serial.begin(9600);
pinMode(irPin1, INPUT);
pinMode(irPin2, INPUT);
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);

}
void loop() {  
  if (!digitalRead(irPin1) && i==1 && state1){
     outsideIr=true;
     delay(100);
     i++;
     state1 = false;
  }
   else if (!digitalRead(irPin2) && i==2 &&   state2){
     Serial.println("Entering inside the room");
     outsideIr=true;
     delay(100);
     i = 1 ;
     count++;
     Serial.print("No. of people inside room: ");
     Serial.println(count);
     state2 = false;
    lightorfanswitch();
    lightorfanswitchOn();
  }
   else if (!digitalRead(irPin2) && i==1 && state2 ){
     outsideIr=true;
     delay(100);
     i = 2 ;
     state2 = false;
  }
  else if (!digitalRead(irPin1) && i==2 && state1 ){
     Serial.println("Exiting from room");
     outsideIr=true;
     delay(100);
     count--;
       Serial.print("No. of people inside room: ");
       Serial.println(count);
     i = 1;
     state1 = false;
     lightorfanswitch();
     lightorfanswitchOFF();
  } 
    if (digitalRead(irPin1)){
     state1 = true;
    }
     if (digitalRead(irPin2)){
     state2 = true;
    } 
    
}


 void lightorfanswitch()
{
    if(count>0) 
    {
     divs=count/5;
    if(count%5>0)
    {
      divs=divs+1;
    }
    if(count>0)
    {
      Serial.print("Count:");
      Serial.println(count);
      Serial.print("No of light:");
      Serial.println(divs);    
      
      delay(2000);
    }
    }
    else
    {
      divs=0;
    }

}

void lightorfanswitchOn()
{
   if(divs>0)
      {
        digitalWrite(2,HIGH);
      }
      if(divs>1)
      {
        digitalWrite(3,HIGH);
      }
      if(divs>2)
      {
        digitalWrite(4,HIGH);
      }
}
void lightorfanswitchOFF()
{
   
   if(divs<1)
      {
         digitalWrite(4,LOW);
        digitalWrite(3,LOW);
        digitalWrite(2,LOW);
      }
      else if(divs<2)
      {
         digitalWrite(4,LOW);
        digitalWrite(3,LOW);
      }
      else if(divs<3)      {
        digitalWrite(4,LOW);

      }

      
}
