extern "c" U8 *strtok(U8 *__str, U8 *__sep);
extern "c" I64 strtoll(U8 *nptr, U8 **endptr, I64 base = 10);
public extern "c" F64 fabs(F64 f1);

Bool isSafe(U8 *);

U0 Main() {
	U8 *delim = "\n";
	U8 *contents = FileRead("test.txt");
	U8 *lines = strtok(contents, delim);
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
	U8 *delim = " ";
	U8 *test = strtok(sequence, delim);
	I64 curr = strtoll(test);
	Bool isIncreasing;
	Bool res = 0;
	Bool isChecked = 0;
	F64 diff;
	I64 prev;
	
	while (curr != NULL) {
		prev = curr;
		test = strtok(NULL, delim);
		curr = strtoll(test, NULL);
		diff = fabs(curr - prev);
		if (diff > 3 || diff < 1) {
			goto end;
		} else if (!isChecked) {
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
	res = 1;
	end:	
		test = NULL;
		return res;
}
