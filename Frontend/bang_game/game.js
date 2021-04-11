var playSound = require("./playSound.js");

var Game = function (
  dice,
  players,
  characterBasedMaxHealth,
  previousObject,
  hydratedAllPlayers
) {
  this.characterBasedMaxHealth = characterBasedMaxHealth;
  this.players = players;
  if (!characterBasedMaxHealth) {
    for (var i = 0; i < this.players.length; i++) {
      this.players.maxHealth = 8;
    }
  }
  if (hydratedAllPlayers !== undefined) {
    this.allPlayers = hydratedAllPlayers;
  } else {
    this.allPlayers = [];
  }
  this.characters = [];
  this.totalArrows = 9;
  this.dice = dice;
  this.wonBy = null;
  this.gatlingAvailable = true;
  if (previousObject !== undefined) {
    this.rehydrate(previousObject);
  }
  this.roles = [
    { name: "Sheriff", imgUrl: "https://i.imgur.com/yYT038yb.jpg" },
    { name: "Deputy", imgUrl: "https://i.imgur.com/6HHgfPab.jpg" },
    { name: "Deputy", imgUrl: "https://i.imgur.com/6HHgfPab.jpg" },
    { name: "Outlaw", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Outlaw", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Outlaw", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Renegade", imgUrl: "https://i.imgur.com/TNeqBpnb.jpg" },
    { name: "Renegade", imgUrl: "https://i.imgur.com/TNeqBpnb.jpg" },
  ];
  var character1 = {
    name: "Джесси Джонес",
    health: 9,
    imgUrl: "https://raw.githubusercontent.com/xex238/Bang/master/images/characters/Main_bang/Bart_Cassidy.jpg",
    abilityDescription:
      "Если осталось 4 хп или меньше, пиво лечит дополнительное очко здоровья.",
  };
  var character2 = {
    name: "Кит Карлсон",
    health: 7,
    imgUrl: "https://i.imgur.com/BZIfBge.png",
    abilityDescription:
      "Каждая карта Гатлинга дает возможность избавиться от карты стрелы.",
  };
  var character3 = {
    name: "Черный Джэк",
    health: 8,
    imgUrl: "https://i.imgur.com/KUrKkis.png",
    abilityDescription:
      "Можно рероллить карты с динамитом. (Если их меньше 3!)",
  };
  var character4 = {
    name: "Русе Дулен",
    health: 9,
    imgUrl: "https://i.imgur.com/Hdcp0p1.png",
    abilityDescription: "Стрелковые карты дают +1 дальности",
  };
  var character5 = {
    name: "Педро Рамирез",
    health: 8,
    imgUrl: "https://i.imgur.com/WcU2f2w.png",
    abilityDescription:
      "Каждое потеряное очко здоровья, дает возможность избавиться от одной карты",
  };
  var character6 = {
    name: "Эль Гринго",
    health: 7,
    imgUrl: "https://i.imgur.com/OF8OH13.png",
    abilityDescription:
      "Когда игрок снимает 1 хп, он вынужден взять карту стрелы",
  };
  var character7 = {
    name: "Барт Кэссэди",
    health: 8,
    imgUrl: "https://i.imgur.com/e8oZGYx.png",
    abilityDescription:
      "Вместо потери хп можно взять карту стрелы (если атакующая карта не динамит или стрела).",
  };
  var character8 = {
    name: "Стервятник Сэм",
    health: 9,
    imgUrl: "https://i.imgur.com/1HkWchT.png",
    abilityDescription: "Получает ХП за каждого убитого игрока",
  };
  var character9 = {
    name: "Безмятежная Джанет",
    health: 8,
    imgUrl: "https://i.imgur.com/OY1CiiX.png",
    abilityDescription: "Стрелковые карты различной дальности взаимозаменяемы",
  };
  var character10 = {
    name: "Джуорданис",
    health: 7,
    imgUrl: "https://i.imgur.com/tXiiB6L.png",
    abilityDescription: "Карты стрел не могут снять больше 1 хп",
  };
  var character11 = {
    name: "Убийца Слэб",
    health: 8,
    imgUrl: "https://i.imgur.com/hlVk73M.png",
    abilityDescription:
      "Раз за ход, вы можете использовать карту пива или стрелкового оружия (любого) дважды.",
  };
  var character12 = {
    name: "Сид Кэтчум",
    health: 8,
    imgUrl: "https://i.imgur.com/cXVoKTA.png",
    abilityDescription:
      "В начале каждого вашего хода вы дает другому игроку экстра хп",
  };
  var character13 = {
    name: "Сьюзи Лафаетт",
    health: 8,
    imgUrl: "https://i.imgur.com/KfiWFxk.png",
    abilityDescription:
      "Если вам не выпала стрелковая карта, то вы получаете хп.",
  };
  var character14 = {
    name: "Пол Регрет",
    health: 9,
    imgUrl: "https://i.imgur.com/UFADg9e.png",
    abilityDescription: "Иммунитет к пулемету Гатлинга",
  };
  var character15 = {
    name: "Удачливый Дюк",
    health: 8,
    imgUrl: "https://i.imgur.com/F6GioiG.png",
    abilityDescription: "Имеете дополнительный реролл",
  };
  var character16 = {
    name: "Пацан Вилли",
    health: 8,
    imgUrl: "https://i.imgur.com/580j9rS.png",
    abilityDescription:
      "Нужно только 2 карты чтобы открыть огонь из Пулемета Гатлинга",
  };
  this.characters = [
    character1,
    character2,
    character3,
    character4,
    character5,
    character6,
    character7,
    character8,
    character9,
    character10,
    character11,
    character12,
    character13,
    character14,
    character15,
    character16,
  ];
};

var getUniqueRandomElement = function (array) {
  var index = Math.floor(Math.random() * array.length);
  var choice = array[index];
  array.splice(index, 1);
  return choice;
};

Game.prototype.rehydrate = function (previousObject) {
 
  this.totalArrows = previousObject.totalArrows;
  this.wonBy = previousObject.wonBy;
  
};

Game.prototype.setup = function () {
  this.assignRoles();
  this.assignCharacters();
  this.setAllHealth();
  this.savePlayers();
  this.rotateSheriffToFirst();
};

Game.prototype.rotateSheriffToFirst = function () {
  var sheriffIndex;
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].role.name === "Sheriff") {
      sheriffIndex = i;
    }
  }
  this.rotatePlayers(sheriffIndex);
};

Game.prototype.setAllHealth = function () {
  for (var i = 0; i < this.players.length; i++) {
    this.players[i].setHealth();
  }
};

Game.prototype.assignRoles = function () {
  for (var i = 0; i < this.players.length; i++) {
    this.players[i].role = getUniqueRandomElement(this.roles);
  }
};

Game.prototype.assignCharacters = function () {
  for (var i = 0; i < this.players.length; i++) {
    this.players[i].character = getUniqueRandomElement(this.characters);
  } //loop
};

Game.prototype.savePlayers = function () {
  if (this.players.length === 8) {
    this.allPlayers = this.players.slice();
  }
};

Game.prototype.rotatePlayers = function (numSteps) {
 
  var loops = numSteps;

  if (numSteps === undefined) {
    loops = 1;
  }
 
  for (var i = 0; i < loops; i++) {
    //2nd array item becomes first - first becomes last:
    this.players.push(this.players.shift());
    // alternative to rotate the other way:
    // last array item becomes first - first becomes 2nd:
    // this.players.unshift(this.players.pop());
  }
};

Game.prototype.nextTurn = function (currentPlayerDead, gameState) {
  this.checkForDeaths();
  //reset health to max in case of overhealing
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].health > this.players[i].maxHealth) {
      this.players[i].health = this.players[i].maxHealth;
    }
  }

  var rotateSteps;
  if (currentPlayerDead === undefined || currentPlayerDead === false) {
    rotateSteps = 1;
  } else {
    rotateSteps = 0;
  }
  this.dice.reset();
  this.gatlingAvailable = true;

  this.rotatePlayers(rotateSteps);
  for (var i = 0; i < this.players.length; i++) {
    this.players[i].target = null;
  }
};
Game.prototype.end = function (winCheckResult) {
  Materialize.toast(winCheckResult, 3000);
  window.alert(winCheckResult);
};

Game.prototype.checkForDeaths = function () {
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].health <= 0) {
    
        this.players[0].target = null;
      }
      this.removePlayer(this.players[i]);
    } // "if health is 0" conditional [end]
  } // for loop [end]
  if (this.winCheck()) {
    this.end(this.winCheck());
  }
  return this.players;
};

Game.prototype.removePlayer = function (player) {
  this.players.splice(this.players.indexOf(player), 1);
  return this.players;
};

Game.prototype.winCheckOutlaws = function () {
  // console.log("outlaw wincheck  checking if array empty - players array length:", this.players.length);
  if (this.players.length === 0) {
    // console.log("game.players.length is 0 - therefore winCheckOutlaws is returning an Outlaw victory");
    return "Outlaws win!";
  }
  // console.log("loops through players array:", this.players, "length:", this.players.length);
  for (var i = 0; i < this.players.length; i++) {
    // console.log("index:", i, "role:", this.players[i].role.name);
    if (this.players[i].role.name === "Sheriff") {
      // console.log("index:", i, "role found:", this.players[i].role.name);
      // console.log("sheriff found, returning null from outlaw wincheck");
      return null;
    }
  }
  // console.log("returning outlaws win because no sheriff found ??");
  return "Outlaws win!";
}; // winConditionOutlaw [end]

Game.prototype.winCheckSheriff = function () {
  var sheriffLives = false;
  var outlawsDead = true;
  var renegadesDead = true;
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].role.name === "Sheriff") {
      var sheriffLives = true;
    } else if (this.players[i].role.name === "Outlaw") {
      outlawsDead = false;
    } else if (this.players[i].role.name === "Renegade") {
      renegadesDead = false;
    }
  } // loop end
  if (sheriffLives && outlawsDead && renegadesDead) {
    return "Sheriff wins!";
  } else {
    return null;
  }
};

Game.prototype.winCheckRenegade = function () {
  if (this.players.length === 1 && this.players[0].role.name === "Renegade") {
    return "Renegade wins!";
  } else {
    return null;
  }
};

Game.prototype.winCheck = function () {
 
  if (this.winCheckSheriff()) {
    this.wonBy = "Sheriff";
    return this.winCheckSheriff();
  }

  var outlawCheckResult = this.winCheckOutlaws();
  var renegadeCheckResult = this.winCheckRenegade();

  if (renegadeCheckResult) {
    this.wonBy = "Renegade";
    return renegadeCheckResult;
  } else if (outlawCheckResult) {
    this.wonBy = "Outlaws";
    return outlawCheckResult;
  }
  return null;
};

Game.prototype.resolveArrows = function () {
  // this.assignArrows();
  for (var i = 0; i < this.dice.arrowsRolled; i++) {
    // console.log("arrows rolled", this.dice.arrowsRolled);
   
    // this.players[0].health = 1
    // this.totalArrows = 1
    this.players[0].arrows += 1;
    this.totalArrows -= 1;
    // throw new Error("giving an arrow")
    // console.log("you got an arrow");
    this.arrowsDamage();
    this.dice.arrowsRolled = 0;
  }
};

Game.prototype.assignArrows = function () {}; // assignArrows = function [end]

Game.prototype.arrowsDamage = function () {
  if (this.totalArrows > 0) return null;
  this.removeHealthAndArrows();
  this.totalArrows = 9;
  Materialize.toast("The Indians have attacked!!", 2000);
  playSound("bow-and-arrows.mp3");
  // console.log("arrows in!");
 
  this.checkForDeaths();
}; // arrowsDamage = function [end]

Game.prototype.removeHealthAndArrows = function () {
  for (var i = 0; i < this.players.length; i++) {
    this.players[i].health -= this.players[i].arrows;
    this.players[i].arrows = 0;
  }
};





Game.prototype.addToActionCounters = function () {
  this.players[0].actionCounters = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
  for (var i in this.dice.all) {
    this.players[0].actionCounters[this.dice.all[i].toString()] += 1;
  }
};


Game.prototype.canHeal = function () {
  if (this.players[0].actionCounters["3"] > 0 && this.players[0].target) {
    return true;
  } else {
    return false;
  }
};

Game.prototype.canShoot = function (distance) {
  if (
    this.players[0].actionCounters[distance.toString()] > 0 &&
    (this.players[0].target === this.players[distance] ||
      this.players[0].target === this.players[this.players.length - distance])
  ) {
    return true;
  } else {
    return false;
  }
}; // canShoot = function [end]

Game.prototype.canShoot1 = function () {
  if (
    this.players[0].actionCounters["1"] > 0 &&
    (this.players[0].target === this.players[1] ||
      this.players[0].target === this.players[this.players.length - 1])
  ) {
    return true;
  } else {
    return false;
  }
};

Game.prototype.canShoot2 = function () {
  if (
    this.players[0].actionCounters["2"] > 0 &&
    (this.players[0].target === this.players[2] ||
      this.players[0].target === this.players[this.players.length - 2])
  ) {
    return true;
  } else if (
    this.players[0].actionCounters["2"] > 0 &&
    this.players.length === 2 &&
    this.players[0].target === this.players[1]
  ) {
    return true;
  } else {
    return false;
  }
};


Game.prototype.canShootTargetCheck = function () {
  return (
    (this.players[0].actionCounters["1"] > 0 &&
      (this.players[0].target === this.players[1] ||
        this.players[0].target === this.players[this.players.length - 1])) ||
    (this.players[0].actionCounters["2"] > 0 &&
      (this.players[0].target === this.players[2] ||
        this.players[0].target === this.players[this.players.length - 2]))
  );
};


Game.prototype.fireGatling = function () {
  $;
  if (this.gatlingCheck()) {
    for (var i = 1; i < this.players.length; i++) {
      this.players[i].health -= 1;
    }
    this.totalArrows += this.players[0].arrows;
    this.players[0].arrows = 0;
    this.gatlingAvailable = false;
    return true;
  } else {
    return false;
  }
};

Game.prototype.gatlingCheck = function () {
  var counter = 0;
  for (item of this.dice.all) {
    if (item === 4) counter++;
  }
  return (
    counter >= 3 && this.gatlingAvailable === true && this.checkActions() <= 0
  );
};

Game.prototype.shootTarget = function () {
  var counterToDecrement;

  if (this.players[0].actionCounters["1"] > 0 && this.canShoot1()) {
    counterToDecrement = 1;
  } else if (this.players[0].actionCounters["2"] > 0 && this.canShoot2()) {
    counterToDecrement = 2;
  }

  if (this.players[0].target) {
    this.players[0].target.health -= 1;
    // console.log(this.players[0].name + " shot " + this.players[0].target.name)
    this.players[0].actionCounters[counterToDecrement.toString()] -= 1;
    // this.checkForDeaths();// need to update the live array if someone dies so that 1s and 2s are still accurate in terms of distance in the same turn as someone dies
  } else {
    // console.log("this is a bug - called shoot function but the button to do that should have been disabled!")
  }

  this.checkForDeaths();

  // console.log("action counters:", this.players[0].actionCounters)
};

Game.prototype.beerTarget = function () {
  if (this.players[0].target) {
    this.players[0].target.health += 1;
    //moving this to next turn, to allow overhealing of someone you don't want to damage before gatlinging them once your dice resolve.
    // if(this.players[0].target.health > this.players[0].target.maxHealth){
    //   this.players[0].target.health = this.players[0].target.maxHealth
    // }
    this.players[0].actionCounters["3"] -= 1;
    // console.log(this.players[0].name + " beer'd " + this.players[0].target.name)
  } else {
    // console.log("you don't have a target to beer! how did you even click the heal button?")
  }
};

Game.prototype.checkActions = function () {
  var counter = 0;
  for (var i = 1; i < 4; i++) {
    if (this.players[0].actionCounters[i.toString()] > 0) {
      counter += this.players[0].actionCounters[i.toString()];
    }
  }
  return counter;
};

Game.prototype.dynamiteExplodes = function () {
  if (this.dice.threeDynamite()) {
    this.players[0].health -= 1;
    return true;
  }
};

module.exports = Game;
module.exports.randomElement = getUniqueRandomElement;
