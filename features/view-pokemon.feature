Feature: View Pokémon
  In order to know about a Pokémon I own
  As a user
  I want to view the Pokémon details including all its attributes

  Background: There is one Pokémon created
    Given Exists a user "username" with password "password"
    And Exists Pokémon registered by "username"
      | nickname   | pokemon   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal

  Scenario: View details for owned Pokémon
    Given I login as user "username" with password "password"
    When I'm viewing the details for the Pokémon "myPokemon"
    Then I'm viewing Pokémon details including
      | nickname   | species   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal