CREATE TABLE 'Entries' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'concept' TEXT NOT NULL,
    'entry' TEXT NOT NULL,
    'date' DATE NOT NULL,
    'mood_id' INTEGER NOT NULL,
    FOREIGN KEY('mood_id') REFERENCES 'Mood'('id')
);
CREATE TABLE 'Moods' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'label' TEXT NOT NULL
);
INSERT INTO Moods
VALUES (1, 'Fine');
INSERT INTO Moods
VALUES (2, 'Proud');
INSERT INTO Moods
VALUES (3, 'Frusturated');
INSERT INTO Moods
VALUES (4, 'Overwhelmed');
INSERT INTO Mood
VALUES (5, 'Happy');
INSERT INTO Mood
VALUES (6, 'Sad');
INSERT INTO Mood
VALUES (7, 'Angry');
INSERT INTO Mood
VALUES (8, 'Ok');
INSERT INTO Entries
VALUES (
        1,
        'Event Listeners',
        'They capture stuff from the dom and send info to other components',
        '2021-02-16',
        2
    );
INSERT INTO Entries
VALUES (
        2,
        'Debugger',
        "The debugger is useful but you have to know where to inset it. \n\nI just debugged code by inserting it in my MoodFilter.js to notice that my return statement wasn't returning code because the code was unreachable",
        '2021-02-16',
        2
    );
INSERT INTO Entries
VALUES (
        3,
        'Deleting',
        'We learned the delete method in fetch calls to delete entries from a database by targeting their id',
        '2021-02-16',
        1
    );
INSERT INTO Entries
VALUES (
    4,
    'JSON',
    'We learned JSON server can do a lot of the heavy lifting for you as long as you know what to ask from it.',
    1598458543321,
    1
);
INSERT INTO Entries
VALUES (
    5,
    'Python',
    'Python is used for a ton of things as it is a versatile programming language based on indentation instead of curly braces',
    1598458543321,
    4
);
INSERT INTO Entries
VALUES (
    6,
    'Server',
    'Apparently back-end means writing the other side of the fetch call',
    1598458543321,
    1
);
INSERT INTO Entries
VALUES (
    7,
    'Network',
    'I learned the network tab in dev tools is useful for viewing the post body being sent to the back end so you know exactly which keys to grab to find values to insert into your database using sequel since sequel requires snake_case and JSON requires camelCase',
    1598458543321,
    1
);
SELECT e.id,
    e.concept,
    e.entry,
    e.mood_id,
    e.date
FROM entries e
WHERE e.id = 2
SELECT m.id,
    m.label
FROM moods m
WHERE m.id = 3


SELECT e.id,
    e.concept,
    e.entry,
    e.mood_id,
    e.date
FROM entries e
WHERE e.concept LIKE '%ugg%'

ALTER TABLE 'Moods' RENAME TO 'Mood'