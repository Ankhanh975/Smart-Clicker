#include <algorithm>
#include <assert.h>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstring>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <list> 
#include <map>
#include <math.h>
#include <memory.h>
#include <queue>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_mixer.h>
#include <SDL2/SDL_ttf.h>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <thread>
#include <time.h>
#include <typeinfo>
#include <unordered_map>
#include <vector>
#include <windows.h>

using namespace std;

void print(int x){ cout << x << "\n"; }
void print(string x){ cout << x << "\n"; }
void print(float x){ cout << x << "\n"; }
void print(double x){ cout << x << "\n"; }

float mapf(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
class color{
  public: 
    unsigned char r,g,b,a;
    color(unsigned char R=0,unsigned char G=0,unsigned char B=0,unsigned char A=255){
      r=R; g=G;  b=B; a=A;
    }
    void overWrite(color OverWriteColor){ //mix 2 color with given alpha
      float factor = OverWriteColor.a / 255.0;
      r = (int) (r * (1 - factor) + OverWriteColor.r * factor);
      g = (int) (g * (1 - factor) + OverWriteColor.g * factor);
      b = (int) (b * (1 - factor) + OverWriteColor.b * factor);
    }
    void setToRandom(){ // Turn this color to total random
      r = rand() % (255 - 1 - 1) + 1 + 1;
      g = rand() % (255 - 1 - 1) + 1 + 1;
      b = rand() % (255 - 1 - 1) + 1 + 1;
    }
    void randomOpset(float percent){ // Set this color trouw some random
      //a1=rand_FloatRange(0, r*percent/100)
      //a2=rand_FloatRange(0, r*percent/100)
      //a3=rand_FloatRange(0, r*percent/100)

      //r+= a1 - r*percent/100/2
      //g+= a2 - g*percent/100/2
      //b+= a3 - b*percent/100/2

      //if (r<0){
      //  r=0;}
      //if (g<0){
      //  g=0;}
      //if (b<0){
      //  b=0;}
    }
};
class Vector{
  public:
    double x=0;
    double y=0;

    Vector(double give_x=0, double give_y=0){
      x=give_x;
      y=give_y;
    }
};

class ScreenControl {
  public:
  	Vector winSize;
  	SDL_Window* window; 
  	SDL_Renderer* renderer; 
  	SDL_Texture* texture;
  	SDL_Event event;
    unsigned char pixels[600 * 600 * 4];

    int frameCount = 0;
    int FrameRate = 60;
    int lastFrame = 0;
    int FrameDelay = 0;
    int FPS = 60;
    const int timePerFrame = 1000/FPS;
    //auto lastFrame = std::chrono::steady_clock::now();

  	ScreenControl(Vector WinSize, const char* title=". ") {
  		winSize = WinSize; //store winSize in memory

      window = SDL_CreateWindow(title,SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,(int) (winSize.x), (int) (winSize.y),SDL_WINDOW_SHOWN);
    	renderer = SDL_CreateRenderer(window,-1,SDL_RENDERER_ACCELERATED);
    	texture = SDL_CreateTexture(renderer ,SDL_PIXELFORMAT_ARGB8888,SDL_TEXTUREACCESS_STREAMING,(int) (winSize.x), (int) (winSize.y));
    	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255 );

      for (int x = 0; x < (int) (winSize.x); ++x)
      {
          for (int y = 0; y < (int) (winSize.x); ++y)
          {
            pixels[(600*4*x)+y*4 + 3 ] = 255;
          }
      }


    }
    void SetIcon(const char* pngPath){
    	SDL_Surface* icon = IMG_Load(pngPath);
      SDL_SetWindowIcon(window, icon);
      SDL_FreeSurface(icon);

    }
    ~ScreenControl(){
    	SDL_DestroyRenderer(renderer );
      SDL_DestroyTexture(texture);
    	SDL_DestroyWindow( window );
    	SDL_Quit();
    }

    void Update(){
    	SDL_UpdateTexture (texture, NULL,&pixels,600 * 4);
      SDL_RenderCopy( renderer, texture, NULL, NULL );
      SDL_RenderPresent( renderer );
      LimitFPS();

      lastFrame = SDL_GetTicks();
      frameCount+=1;
    }

    void put_Pixel(int x, int y, color Color){ 
      if (x>=0 && x<(winSize.x) && y>=0 && y<(winSize.y))
      {
          long XY = (600*4*y)+x*4;
          color DisplayColor(pixels[ XY+0 ],pixels[ XY+1 ],pixels[ XY+2 ]);
          DisplayColor.overWrite(Color);

            pixels[ XY+2 ] = DisplayColor.r;
            pixels[ XY+1 ] = DisplayColor.g;
            pixels[ XY+0 ] = DisplayColor.b;
            //pixels[ XY+3 ] = Color.a;

        
        }
      }

      void backgruond(color Color){
        //for (int x = 0; x < (int) (winSize.x); ++x)
        //{
        //  for (int y = 0; y < (int) (winSize.x); ++y)
        //  {
        //    put_Pixel(x,y, Color);
        //  }
        //}

    }
    

    void LimitFPS(){
    	//std::chrono::duration<double> now = std::chrono::steady_clock::now();

    	//std::chrono::duration<double> runtime = now - lastFrame;

    	//runtime.count();

    	int startTime = lastFrame;
      int endTime = SDL_GetTicks();
      FrameDelay= endTime- startTime;
      if (FrameDelay < timePerFrame) {
            SDL_Delay(timePerFrame - FrameDelay);
            
        }

      
    }

    int GetFPS(bool TakeAng = false){
        if (TakeAng)
        {
          /* code */
        }else{
          //return mapf(FrameDelay) ;

        }
        return 0;
    }
};
class DrawLib{
	//color FillColor;
	//color StrokeColor;
	//Vector Translate;
	double rotateAngle;

  void rotate(float ang){

  }
	void push(){

	}
	void pop(){
		
	}
	void Ellipse(){

	}
	void Rectangle(){

	}
	void Triangle(){

	}
	void Line(){

	}
	void Point(){

	}
	void Quadrilateral(){

	}
	void Arc(){

	}
  void DisplayFPS(){
    
  }
};

typedef unsigned long long int UINT64;

UINT64 randint(UINT64 const& min = 0, UINT64 const& max = 0)
{
    return (((UINT64)(unsigned int)rand() << 32) + (UINT64)(unsigned int)rand()) % (max - min) + min;
}
float rand_FloatRange(float a, float b)
{
    return ((b - a) * ((float)rand() / RAND_MAX)) + a;
}

void setup(){
  if (SDL_Init(SDL_INIT_EVERYTHING) > 0)
    std::cout << "SDL_ERROR: " << SDL_GetError() << std::endl;

  if (!(IMG_Init(IMG_INIT_PNG)))
    std::cout << "IMG_init has failed. Error: " << SDL_GetError() << std::endl;
  TTF_Init();

  srand((int)time(0));



  //IMG_Init(IMG_INIT_PNG);
    //SDL_Surface* Icon = IMG_Load( "Logo.png" );

    //SDL_SetWindowMinimumSize(Screen.window,100,100);
    //SDL_SetWindowMaximumSize(Screen.window,1000,1000);
}



int main(int argc, char* argv[] )
{   
  setup();
  int MouseX=0;
  int MouseY=0;

  Vector winSize(600,600);
  ScreenControl Screen(winSize, "Smart Clicker");
  

  color Backgruond(200,200,200);

  bool running = 1;
  while(running){
 		while( SDL_PollEvent(&Screen.event) ){
          if (Screen.event.type==SDL_QUIT){
              running = 0;
              break;
          }
          if (Screen.event.type==SDL_KEYDOWN){
              int KeyDown=Screen.event.key.keysym.sym;

          }
          if (Screen.event.type==SDL_MOUSEMOTION){
              MouseX = Screen.event.motion.x;
              MouseY = Screen.event.motion.y;

          }

        }
    
     //do something here
     for (int x = 0; x < 600; ++x)
     {
       for (int y= 0; y < 600; ++y)
       {

         Screen.put_Pixel(x,y, Backgruond);
       }
     }
     //
     Screen.Update();
   }

	return 0;
}