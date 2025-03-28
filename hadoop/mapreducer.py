hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
 -files mapper.py,reducer.py \
 -mapper "/usr/bin/python3 mapper.py" \
 -reducer "/usr/bin/python3 reducer.py" \
 -input /tmp/big_datajan2025/demo/text1.txt\
 -output /tmp/big_datajan2025/demo/new3

#!/usr/bin/env python
import sys

# Mapper function to read input lines, split into words, and emit word counts
def mapper():
    for line in sys.stdin:
        # Strip leading/trailing spaces and split the line into words
        line = line.strip()
        words = line.split()
        
        for word in words:
            # Output the word with count 1
            print(f"{word.lower()}\t1")

if _name_ == "__main__":
    mapper()

#!/usr/bin/env python
import sys

# Reducer function for CSV processing (aggregation)
def reducer():
    current_key = None
    current_sum = 0.0

    for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t', 1)

        try:
            value = float(value)
        except ValueError:
            continue  # Skip lines where value can't be converted to float

        if current_key == key:
            current_sum += value
        else:
            if current_key:
                # Emit the previous key and its summed value
                print(f"{current_key}\t{current_sum}")
            current_key = key
            current_sum = value

    # Emit the last key and its summed value
    if current_key == key:
        print(f"{current_key}\t{current_sum}")

if _name_ == "__main__":
    reducer()
