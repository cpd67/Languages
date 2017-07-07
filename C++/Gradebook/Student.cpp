#include "Student.h"

Student::Student() {
  myName = "Default student";
  myAverage = 0.0;
  myNumAssessments = 0;
  myScores = NULL;
}

Student::Student(string name, int numAssessments) {
  myName = name;
  myAverage = 0.0;
  myNumAssessments = numAssessments;
  myScores = new float[myNumAssessments];
  // Zero out the scores array
  for(int i = 0; i < myNumAssessments; i++) {
    myScores[i] = 0.0;
  }
}

// Accessor for name of student
string Student::getName() const {
  return myName;
}

// Mutator for assessment score
void Student::setScore(int assessNum, float score) {
  myScores[assessNum] = score;
  //Recompute the average for the student
  computeAverage();
}

// Private method that calculates the average grade for a student
void Student::computeAverage() {
  float sum = 0.0;
  for(int i = 0; i < myNumAssessments; i++) {
    sum += myScores[i];
  }
  myAverage = (sum/myNumAssessments);
}
