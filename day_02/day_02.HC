// import C library functions
extern "c" U8 *strtok(U8 *__str, U8 *__sep);
extern "c" I64 strtoll(U8 *nptr, U8 **endptr, I64 base = 10);
public extern "c" F64 fabs(F64 f1);

Bool isSafe(U8 *);

U0 Main() {
	// split file on delimiter
	U8 *delim = "\n";
	U8 *contents = FileRead("test.txt");
	U8 *lines = strtok(contents, delim);

	// total for part 1
	I64 total1 = 0;

	while (lines != NULL) {
		"lines: %s\n", lines;
		if (isSafe(lines)) {
			total1++;
		}
		lines = strtok(NULL, delim);
	}

	"Part 1: %d\n", total1;
}

Bool isSafe(U8 *sequence) {
	// split sequence on delimiter
	U8 *delim = " ";
	U8 *currStr = strtok(sequence, delim);

	// convert current number to int64
	I64 curr = strtoll(test);

	// helper vars
	Bool res = 0;
	Bool isChecked = 0;
	Bool isIncreasing;
	F64 diff;
	I64 prev;
	
	while (curr != NULL) {
		// load next number and find difference
		prev = curr;
		currStr = strtok(NULL, delim);
		curr = strtoll(currStr, NULL);
		diff = fabs(curr - prev);
		
		if (diff > 3 || diff < 1) {
			goto end;
		} else if (!isChecked) {
			// check increasing/decreasing
			if (curr > prev) {
				isIncreasing = 1;
			} else if (curr < prev) {
				isIncreasing = 0;
			} else {
				goto end;
			}
			isChecked = 1;
		} else if (curr == prev || curr > prev != isIncreasing) {
			goto end;
		} 
	}
	// return true if no violations
	res = 1;
	end:	
		// allocate NULL for safety
		test = NULL;
		return res;
}
