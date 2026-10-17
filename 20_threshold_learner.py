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
# new_messages = [2, 9, 0, 3]
test = [(2, "not_spam"), (8, "spam"), (1, "not_spam"), (3, "spam"), (5, "spam")]


def predict(count, threshold):
    return "spam" if count >= threshold else "not_spam"


def evaluate(examples, threshold):
    amount = 0
    for count, label in examples:
        if predict(count, threshold) == label:
            amount += 1
    return amount


def train(examples):
    best_threshold = None
    best_correct = -1

    for threshold in range(9):
        correct = evaluate(examples, threshold)

        if correct > best_correct:
            best_correct = correct
            best_threshold = threshold

    return (best_threshold, best_correct)


threshold, train_score = train(training)
test_score = evaluate(test, threshold)
print(f"train: {train_score}/{len(training)}, test: {test_score}/{len(test)}")
# print(threshold, score)

# for message in new_messages:
#     print(predict(message, threshold))
