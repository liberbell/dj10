function sleepIn(weekday, vacation) {
    return (!weekday || vacation);
}

function monkeyTrouble(aSmile, bSmile) {
    return (aSmile && bSmile) || (!aSmile && !bSmile);
}

function stringTimes(str, n) {
    var retrunSTR = "";
    var i = 0;
    while (i < n) {
        retrunSTR += str;
        i ++;
    }
    return retrunSTR;
}

function luckySum(a, b, c) {
    if (a == 13) {
        return 0;
    }
    if (b == 13) {
        return a;
    }
    if (c == 13) {
        return a + b;
    }
}

function caught_speeding(speed, is_birthday) {
    
}