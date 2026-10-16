training = [
    (0, "not_spam"),
    (1, "not_spam"),
    (5, "spam"),
    (2, "not_spam"),
    (4, "spam"),
    (6, "spam"),
    (3, "spam"),
    (1, "not_spam"),
    (0, "spam"),
    (7, "spam"),
]
new_messages = [2, 9, 0, 3]


def predict(count, threshold):
    return "spam" if count >= threshold else "not_spam"


def train(examples):
    best_threshold = None
    best_correct = -1

    for threshold in range(9):
        correct = 0
        for count, label in examples:
            if predict(count, threshold) == label:
                correct += 1

        if correct > best_correct:
            best_correct = correct
            best_threshold = threshold

    return (best_threshold, best_correct)


threshold, score = train(training)
print(threshold, score)

for message in new_messages:
    print(predict(message, threshold))
