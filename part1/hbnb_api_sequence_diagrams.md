# HBnB API Sequence Diagrams

This document contains sequence diagrams for four main API calls in the HBnB application, showing interactions between Presentation, Business Logic, and Persistence layers.

---

## 1. User Registration
**Purpose:** Allows a new user to sign up for an account.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: POST /register with user data
API->>BusinessLogic: validateInput(userData)
BusinessLogic->>Database: checkUserExists(email)
Database-->>BusinessLogic: return exists/not exists
alt user does not exist
    BusinessLogic->>Database: saveNewUser(userData)
    Database-->>BusinessLogic: confirmSave
    BusinessLogic-->>API: registrationSuccess
else user exists
    BusinessLogic-->>API: registrationFailed
end
API-->>User: return success/failure response
```

---

## 2. Place Creation
**Purpose:** Allows a user to create a new place listing.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: POST /places with place data
API->>BusinessLogic: validatePlaceData(placeData)
BusinessLogic->>BusinessLogic: checkUserAuthentication(user)
BusinessLogic->>Database: savePlace(placeData)
Database-->>BusinessLogic: confirmSave
BusinessLogic-->>API: creationSuccess
API-->>User: return success/failure response
```

---

## 3. Review Submission
**Purpose:** Allows a user to submit a review for a place.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: POST /places/:id/review with reviewData
API->>BusinessLogic: validateReview(reviewData)
BusinessLogic->>BusinessLogic: checkUserAuthentication(user)
BusinessLogic->>Database: saveReview(placeId, reviewData)
Database-->>BusinessLogic: confirmSave
BusinessLogic-->>API: reviewSuccess
API-->>User: return success/failure response
```

---

## 4. Fetching a List of Places
**Purpose:** Retrieves a list of places based on user-provided criteria.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: GET /places?criteria
API->>BusinessLogic: validateQuery(criteria)
BusinessLogic->>Database: fetchPlaces(criteria)
Database-->>BusinessLogic: placeList
BusinessLogic-->>API: formattedPlaceList
API-->>User: return place list
```

---

## Explanatory Notes
- **Presentation Layer (API):** Handles incoming requests, validates input, and returns responses to the client.
- **Business Logic Layer:** Manages authentication, authorization, data validation, and coordinates processing with the database.
- **Persistence Layer (Database):** Responsible for storing, retrieving, and confirming data for users, places, and reviews.

All diagrams clearly show the flow from user request to database interaction and back to the user.

