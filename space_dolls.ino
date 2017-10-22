const byte dolls = 9;
const byte idx = 0;
int pins[dolls] = {PB12, PB13, PB14, PB15, PA8, PA9, PA10, PB6, PB7};

int lastI;
int lastX;
int timeElapsed = 0;

int state[dolls][dolls];

void setup() {
  Serial.begin(9600);
  for (byte c=0; c<dolls; c++) {
    pinMode(pins[c], INPUT_PULLUP);
    for (byte d=0; d<dolls; d++) {
      state[c][d] = 0;
    }
  }
}

void loop() {
  delay(100);
  for (byte c=0; c<dolls; c++) {
    pinMode(pins[c], OUTPUT);
    digitalWrite(pins[c], LOW);
    delay(10);
    for (byte r=0; r<dolls; r++) {
      if (r != c) {
        int i = min(r, c);
        int x = max(r, c);
        int s = state[i][x];
        if (digitalRead(pins[r])==LOW) {
          if (s != 1) {
            state[i][x] = 1;
            if (!(lastI == i && lastX == x) || timeElapsed > 5000) {
              Serial.print(i);
              Serial.print(" ");
              Serial.print(x);
              Serial.print("\n");
              timeElapsed = 0;
            }
            lastI = i;
            lastX = x;
          }
        } else {
          if (s != 0) {
            state[i][x] = 0;
          }
        }
      }
    }
    timeElapsed = timeElapsed + 100;
    pinMode(pins[c], INPUT_PULLUP);
  }
}
