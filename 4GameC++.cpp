#include <iostream>

using namespace std;

int main()
{
    int g[16]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    cout <<"| "<<g[0]<<"  | "<<g[1]<<"  | "<<g[2]<<"  | "<<g[3]<<"  |"<<endl;
    cout <<"____________________________"<<endl;
    cout <<"| "<<g[4]<<"  | "<<g[5]<<"  | "<<g[6]<<"  | "<<g[7]<<"  |"<<endl;
    cout <<"____________________________"<<endl;
    cout <<"| "<<g[8]<<"  | "<<g[9]<<" | "<<g[10]<<"| "<<g[11]<<"  |"<<endl;
    cout <<"____________________________"<<endl;
    cout <<"| "<<g[12]<<" | "<<g[13]<<" | "<<g[14]<<" | "<<g[15]<<" |"<<endl;
    cout <<"____________________________"<<endl;
    int i=0;
    int x=0;
    int y=0;
    int z=0;
    int p1,p2;
    while (i<8){
        while (x<4){
            cout <<"player 1:"<<endl;
            cout <<"Enter the first square:";
            cin >>p1;
            cout <<endl<<"Enter the second square:";
            cin >>p2;
            if ((p1==p2+1 || p1==p2-1 || p1==p2+4 || p1==p2-4) &&((p1!= 4 || p2 != 5)&&(p1 != 8 || p2 != 9)&&(p1 != 12 || p2 != 13) &&(p1 != 5 || p2 != 4) && (p1 != 9 || p2 != 8) && (p1 != 13 || p2 != 12))&&( g[p1-1]!=0 && g[p2-1]!=0)){
                g[p1 - 1] = 0;
                g[p2 - 1] = 0;
                cout <<"| "<<g[0]<<"  | "<<g[1]<<"  | "<<g[2]<<"  | "<<g[3]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[4]<<"  | "<<g[5]<<"  | "<<g[6]<<"  | "<<g[7]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[8]<<"  | "<<g[9]<<" | "<<g[10]<<"| "<<g[11]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[12]<<" | "<<g[13]<<" | "<<g[14]<<" | "<<g[15]<<" |"<<endl;
                cout <<"____________________________"<<endl;
                x++;
                i++;
            }
            else {
                for (int l=4;l<12;l++){
                    if (g[l] != g[l+1]  || g[l] != g[l-1] || g[l] != g[l+4]  || g[l] != g[l- 4]){
                        z++;

                    }
                }
                if (z>=8){
                    cout <<"Try again"<<endl;
                    z=0;

                    continue;
                }
                else {
                    if (x>y){
                        cout <<"Player 1 wins"<<endl;
                        return 0;
                    }
                    else {
                        cout<<"Player 2 wins"<<endl;
                        return 0;
                    }

                }

            }
        break;
        }
        while (y<4){
            cout <<"player 2:"<<endl;
            cout <<"Enter the first square:";
            cin >>p1;
            cout <<endl<<"Enter the second square:";
            cin >>p2;
            if ((p1==p2+1 || p1==p2-1 || p1==p2+4 || p1==p2-4) &&((p1!= 4 || p2 != 5)&&(p1 != 8 || p2 != 9)&&(p1 != 12 || p2 != 13) &&(p1 != 5 || p2 != 4) && (p1 != 9 || p2 != 8) && (p1 != 13 || p2 != 12))&&( g[p1-1]!=0 && g[p2-1]!=0)){
                g[p1 - 1] = 0;
                g[p2 - 1] = 0;
                cout <<"| "<<g[0]<<"  | "<<g[1]<<"  | "<<g[2]<<"  | "<<g[3]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[4]<<"  | "<<g[5]<<"  | "<<g[6]<<"  | "<<g[7]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[8]<<"  | "<<g[9]<<" | "<<g[10]<<"| "<<g[11]<<"  |"<<endl;
                cout <<"____________________________"<<endl;
                cout <<"| "<<g[12]<<" | "<<g[13]<<" | "<<g[14]<<" | "<<g[15]<<" |"<<endl;
                cout <<"____________________________"<<endl;
                y++;
                i++;
            }
            else {
                for (int l=4;l<12;l++){
                    if (g[l] != g[l+1]  || g[l] != g[l-1] || g[l] != g[l+4]  || g[l] != g[l- 4]){
                        z++;

                    }
                }
                if (z>=8){
                    cout <<"Try again"<<endl;
                    z=0;
                    continue;
                }
                else {
                    if (x>y){
                        cout <<"Player 1 wins"<<endl;
                        return 0;
                    }
                    else {
                        cout<<"Player 2 wins"<<endl;
                        return 0;
                    }

                }
            }
        break;
        }
    }


cout << "player 2 wins"<<endl;
return 0;
}


