from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext("local[3]","word count")
    sc.setLogLevel("Error")

    lines = sc.textFile("text_count.txt")

    words = lines.flatMap(lambda line : line.split(" "))

    wordsCounts = words.countByValue()
    for word, count in wordsCounts.items():
        print("{}: {}".format(word, count))
