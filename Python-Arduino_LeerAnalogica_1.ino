char car;
int val;

void setup() {
  Serial.begin(9600);
  

}

void loop() {
  if(Serial.available()>0)
  {
    car = Serial.read();
    if(car == 'r')
    {
      val = analogRead(A0);
      Serial.println(val);
    }
  }

}
