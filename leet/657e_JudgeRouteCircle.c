/* 657 - Leet Code */
bool judgeCircle(char* moves) {
    int x=0, y=0;
    
    while(*moves != '\0') {
        switch(*moves) {
            case 'U': y++; break;
            case 'D': y--; break;
            case 'R': x++; break;
            case 'L': x--; break;
        }
        moves++;
    }
    
    return (x==0 && y==0);
}
