export {};

const inFile = Bun.file("input.txt");

inFile.text().then(text => {
    const lines = text.split('\r\n');

    var result = 0;

    lines.forEach(line => {
        const numbers = line.split(' ').map(el => parseInt(el));
        const increasing = (numbers[1] - numbers[0]) > 0;
        var safe = true;

        for(var i = 1; i < numbers.length; ++i) {
            const diff = numbers[i] - numbers[i-1];
            const absDiff = Math.abs(diff);

            if (absDiff == 0 || absDiff > 3 || (diff > 0 !== increasing)) {
                safe = false;
                break;
            }
        }
    
        if (safe) {
            result++;
        }
    });

    console.log(result);
});
