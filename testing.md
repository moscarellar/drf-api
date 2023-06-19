#API Manual Testing

## Methodology

All users should be able to create events, but should only be able to invite users from their own tribe, and events should only be viewable by members of the same tribe. Users should be able to edit events they created but not those created by other users, except the tribe admin who should be able to edit all events created by members of their tribe.

Notifications are created programatically. Only the recipient of a notification should be able to delete it.

Users should be able to edit their own profiles, but not those of other users, except for the tribe admin who should be able to edit profiles for all members of their tribe (but not those for members of other tribes). Users should be able to delete their own profiles and deactivate their accounts, but not those of other users, except for the tribe admin who should be able to close the accounts of other users who are part of their tribe.

Please note that object id numbers used in the tests may vary in the screenshots and in the current state of the database, because some of the tests involved permanent deletion of objects, with similar objects subsequently recreated to continue testing.

Tests were performed using the Django Rest Framework HTML interface running on a test server. Each endpoint has a heading below, with the corresponding tests and results.

## Table of contents

- [POST](#--accounts-tribe--post)
  * [Test 1](#test-1)


- [POST](#--accounts-user---post)
  * [Test 7](#test-7)

-

## POST

### Test 1
When unauthenticated, a POST request to this endpoint with the following data should result in creation of new user 'chief1', a new user profile linked to 'chief1' *with family admin status* and a new tribe called 'Tribe1'. Should return HTTP status 201.


**Result: PASS**

<p align="center">
    <img src="/testing.png" width=800>
</p>


