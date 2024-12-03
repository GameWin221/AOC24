export {};

function verify(numbers: Array<number>, removed: boolean) {
    const increasing = (numbers[1] - numbers[0]) > 0;
    
    for(var i = 1; i < numbers.length; ++i) {
        const diff = numbers[i] - numbers[i-1];
        const absDiff = Math.abs(diff);

        if (absDiff == 0 || absDiff > 3 || (diff > 0 !== increasing)) {
            if (removed) {
                return false;
            } else {
                return (
                    verify(numbers.slice(0, i).concat(numbers.slice(i+1, numbers.length)), true) || 
                    verify(numbers.slice(0, i-1).concat(numbers.slice(i, numbers.length)), true)
                )
            }
        }
    }

    return true;
}

const inFile = Bun.file("input.txt");

inFile.text().then(text => {
    const lines = text.split('\r\n');

    var result = 0;
    
    lines.forEach(line => {
        const numbers = line.split(' ').map(el => parseInt(el));

        if (verify(numbers, false) || verify(numbers.slice(1, numbers.length), true)) {
            //console.log(numbers);
            result++;
        }
    });

    console.log(result);
});
