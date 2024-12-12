import pandas as pd
import random

# Full list of good feedback phrases
good_feedback_phrases = [
    "All good",
    "your teaching is excellent",
    "Exceptional teacher who inspires critical thinking",
    "Explains complex concepts with remarkable clarity",
    "Demonstrates deep subject matter expertise",
    "Innovative teaching methods that promote deep understanding",
    "Provides clear and detailed explanations",
    "Creates interactive and dynamic classroom experiences",
    "Adapts teaching style to different learning needs",
    "Brings real-world expertise into classroom discussions",
    "Challenges students to think critically and creatively",
    "Masters the art of making difficult topics easily comprehensible",
    "Uses engaging multimedia resources to enhance learning",
    "Consistently updates course content with latest industry trends",
    "Balances theoretical knowledge with practical applications",
    "Demonstrates exceptional subject matter mastery",
    "Creates thought-provoking learning experiences",
    "Encourages collaborative learning among peers",
    "Promotes hands-on activities that enhance understanding",
    "Provides inspiring and motivational classroom discussions",
    "Uses a variety of assessment methods to gauge understanding",
    "Fosters a growth mindset among students",
    "Creates a welcoming environment for all students",
    "Balances individual attention with group learning activities",
    "Incorporates cutting-edge research into the curriculum",
    "Instills confidence in students to tackle challenging problems",
    "Explains abstract ideas with relatable, practical examples",
    "Encourages innovative thinking through thought-provoking questions",
    "Establishes clear connections between theory and real-world applications",
    "Inspires a passion for lifelong learning in students",
    "Integrates interdisciplinary perspectives for holistic understanding",
    "Utilizes adaptive technologies to personalize learning experiences",
    "Facilitates peer-to-peer learning to reinforce concepts",
    "Engages students through immersive and experiential activities",
    "Encourages self-directed exploration of advanced topics",
]

# Full list of bad feedback phrases
bad_feedback_phrases = [
    "Lacks clarity in explaining course material",
    "Fails to explain complex concepts effectively",
    "Lectures are monotonous and difficult to follow",
    "Demonstrates insufficient subject matter knowledge",
    "Uses outdated teaching methods and resources",
    "Provides confusing and unclear instructions",
    "Fails to maintain student engagement",
    "Delivers lectures without enthusiasm or passion",
    "Relies too heavily on textbook content",
    "Presents information in a dry and uninteresting manner",
    "Fails to adapt teaching style to student needs",
    "Lacks depth in course content presentation",
    "Provides incomplete or fragmented explanations",
    "Demonstrates limited understanding of subject matter",
    "Uses overly complex language that confuses students",
    "Creates an unapproachable atmosphere for students",
    "Does not provide timely feedback on assignments",
    "Fails to create clear connections between topics",
    "Expects unrealistic levels of prior knowledge",
    "Ignores suggestions for improvement from students",
    "Does not encourage classroom participation",
    "Leaves questions unanswered or dismisses them",
    "Focuses too much on theory with no practical examples",
    "Uses disorganized slides and materials that confuse students",
    "Fails to update course content to reflect current trends",
    "Frequently digresses into irrelevant topics, losing focus",
    "Overwhelms students with excessive and poorly explained content",
    "Neglects to provide context for complex ideas",
    "Fails to address varying levels of student preparedness",
    "Uses ineffective examples that do not clarify the material",
    "Appears unapproachable and discourages questions",
    "Presents conflicting or contradictory information",
    "Assigns tasks without providing adequate instructions",
    "Does not create opportunities for collaborative learning",
    "Lacks awareness of students' progress and struggles",
]

def generate_unique_feedback_dataset():
    """
    Generates a dataset of 500 unique feedback rows, alternating good and bad feedback.
    Returns:
        pd.DataFrame: DataFrame containing the dataset.
    """
    data = []
    good_used = set()
    bad_used = set()

    for i in range(1000):  # Reduced to 500 rows
        if i % 2 == 0:  # Good feedback
            if len(good_used) == len(good_feedback_phrases):
                good_used.clear()  # Reset when all good phrases are used
            while True:
                feedback = random.choice(good_feedback_phrases)
                if feedback not in good_used:
                    good_used.add(feedback)
                    rating = random.choice([4, 5])
                    break
        else:  # Bad feedback
            if len(bad_used) == len(bad_feedback_phrases):
                bad_used.clear()  # Reset when all bad phrases are used
            while True:
                feedback = random.choice(bad_feedback_phrases)
                if feedback not in bad_used:
                    bad_used.add(feedback)
                    rating = random.choice([1, 2, 3])
                    break

        # Append data
        data.append([i + 1, rating, feedback])

    # Create DataFrame
    df = pd.DataFrame(data, columns=['Student_ID', 'Rating', 'Feedback_Text'])

    # Save to CSV
    df.to_csv('teacher_feedback_dataset_1000.csv', index=False)

    return df

# Generate the dataset
feedback_df = generate_unique_feedback_dataset()

# Display the first few rows
print(feedback_df.head(10))
print("\nDataset shape:", feedback_df.shape)
