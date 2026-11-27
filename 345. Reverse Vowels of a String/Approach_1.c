char* reverseVowels(char* s) {
    int size = strlen(s) / sizeof(char);
    int si = 0;
    int ei = size -1;
    while(si < ei){
        if (s[ei] != 'a' && s[ei] != 'e' && s[ei] != 'i' && s[ei] != 'o' && s[ei] != 'u' && s[ei] != 'A' && s[ei] != 'E' && s[ei] != 'I' && s[ei] != 'O' && s[ei] != 'U'){
            ei--;
            continue;
        }else if (s[si] == 'a' || s[si] == 'e' || s[si] == 'i' || s[si] == 'o' || s[si] == 'u' || s[si] == 'A' || s[si] == 'E' || s[si] == 'I' || s[si] == 'O' || s[si] == 'U'){
            char temp = s[si];
            s[si] = s[ei];
            s[ei] = temp;
            ei--;
        }

        si++;
    }

    return s;
}