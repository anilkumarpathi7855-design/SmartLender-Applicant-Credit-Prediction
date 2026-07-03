# Test Cases - Smart Lender Applicant Credit Prediction

## Test Case 1
**Test ID:** TC_01

**Objective:** Verify home page loads successfully.

**Input:** Open application URL.

**Expected Result:** Home page should open without errors.

**Status:** Pass

---

## Test Case 2
**Test ID:** TC_02

**Objective:** Verify prediction with valid applicant details.

**Input:**
- Gender: Male
- Married: Yes
- Applicant Income: 5000
- Loan Amount: 120

**Expected Result:** Loan prediction should be displayed.

**Status:** Pass

---

## Test Case 3
**Test ID:** TC_03

**Objective:** Verify mandatory field validation.

**Input:** Leave required fields empty.

**Expected Result:** Application should not accept empty values.

**Status:** Pass

---

## Test Case 4
**Test ID:** TC_04

**Objective:** Verify model prediction.

**Input:** Valid applicant data.

**Expected Result:** Display Loan Approved or Loan Rejected.

**Status:** Pass
