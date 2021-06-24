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
    { name: "Шерифф", imgUrl: "https://i.imgur.com/yYT038yb.jpg" },
    {
      name: "Помощник Шериффа",
      imgUrl: "https://i.imgur.com/6HHgfPab.jpg",
    },
    {
      name: "Помощник Шериффа",
      imgUrl: "https://i.imgur.com/6HHgfPab.jpg",
    },
    { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
    { name: "Ренегат", imgUrl: "https://i.imgur.com/TNeqBpnb.jpg" },
    { name: "Ренегат", imgUrl: "https://i.imgur.com/TNeqBpnb.jpg" },
  ];
  var character1 = {
    name: "Джесси Джонес",
    health: 9,
    imgUrl: "../Main_bang/Jesse_Jones.jpg",
    abilityDescription:
      "Если меньше 4хп, то пиво дает +2 хп (только для себя).",
  };
  var character2 = {
    name: "Кит Карслон",
    health: 7,
    imgUrl: "../Main_bang/Kit_Carison.jpg",
    abilityDescription: "Обмен карт гатлинга на карты стрел (с любого игрока)",
  };
  var character3 = {
    name: "Блэк Джэк",
    health: 8,
    imgUrl: "../Main_bang/Black_Jack.jpg",
    abilityDescription: "Можно пересдавать карты динамита",
  };
  var character4 = {
    name: "Рус Дуулэн",
    health: 9,
    imgUrl: "../Main_bang/Rose_Doolan.jpg",
    abilityDescription: "Стрелковые карты имеют +1 дальность.",
  };
  var character5 = {
    name: "Педро Рамирез",
    health: 8,
    imgUrl: "../Main_bang/Pedro_Ramirez.jpg",
    abilityDescription:
      "За каждое потерянное очко здоровья, можно избавиться от одной карты стрелы.",
  };
  var character6 = {
    name: "Эль Гринго",
    health: 7,
    imgUrl: "../Main_bang/El_Gringo.jpg",
    abilityDescription:
      "За каждое потеряное вами здоровье, другой игрок берет стрелу",
  };
  var character7 = {
    name: "Барт Кэссэди",
    health: 8,
    imgUrl: "../Main_bang/Bart_Cassidy.jpg",
    abilityDescription:
      "Вы можете принять карты стрелы вместо потери здоровья (кроме случая набега индейцев или взрыва динамита).",
  };
  var character8 = {
    name: "Стервятник Сэм",
    health: 9,
    imgUrl: "../Main_bang/Vulture_Sam.jpg",
    abilityDescription: "Получаете очко здоровья за каждое убийство",
  };
  var character9 = {
    name: "Мерзкая Джанет",
    health: 8,
    imgUrl: "../Main_bang/Calamity_Janet.jpg",
    abilityDescription: "Стрелковые карты взаимозаменяемы",
  };
  var character10 = {
    name: "Человек без имени",
    health: 7,
    imgUrl: "../Main_bang/Jourdonnais.jpg",
    abilityDescription:
      "Вы можете потерять не больше 1 очка здоровья при набеге индейцев",
  };
  var character11 = {
    name: "Убийца Слэб",
    health: 8,
    imgUrl: "../Main_bang/Slab_the_Killer.jpg",
    abilityDescription:
      "Раз в ход можно удваивать стрелковые карты за счет карты пива",
  };
  var character12 = {
    name: "Сид Кэтчум",
    health: 8,
    imgUrl: "../Main_bang/Sid_Ketchum.jpg",
    abilityDescription: "В начале каждого хода даете хп любому игроку.",
  };
  var character13 = {
    name: "Сьюзи Лафаетт",
    health: 8,
    imgUrl: "../Main_bang/Suzy_Lafayette.jpg",
    abilityDescription: "Если нет стрелковых карт, то получаете хп",
  };
  var character14 = {
    name: "Пол Регрет",
    health: 9,
    imgUrl: "../Main_bang/Paul_Regret.jpg",
    abilityDescription: "Не теряете очки здоровья при огне Пулемета Гатлинга.",
  };
  var character15 = {
    name: "Удачливый Дюк",
    health: 8,
    imgUrl: "../Main_bang/Lucky_Duke.jpg",
    abilityDescription: "Вы имеет одну дополнительную пересдачу карт.",
  };
  var character16 = {
    name: "Малыш Вилли",
    health: 8,
    imgUrl: "../Main_bang/Willy_the_Kid.jpg",
    abilityDescription: "Нужно только 2 карты гатлинга чтобы открыть огонь",
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
  // this.characterBasedMaxHealth = previousObject.characterBasedMaxHealth;
  // if (!this.characterBasedMaxHealth){
  //   for (var i = 0; i < this.players.length; i++){
  //     this.players[i].maxHealth = 8;
  //   }
  // }
  this.totalArrows = previousObject.totalArrows;
  this.wonBy = previousObject.wonBy;
  // console.log(this.players);

  // this.allPlayers = originalOrderPlayers;
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
    if (this.players[i].role.name === "Шерифф") {
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
  // rotates the array the number of times that is passed as an argument
  // if no argument is passed, the OR operator will set loops to 1 as numSteps will be undefined, which is falsey
  var loops = numSteps;

  if (numSteps === undefined) {
    loops = 1;
  }
  // ^ this could have been written:
  // - which might be better - passing 0 in deliberately would cause the loops to be set to 1, not 0, when using the OR operator method above - but there's no need to ever rotate the players array 0 times
  // if (numSteps === undefined){
  //   var loops = 1;
  // }
  // else{
  //   var loops = numSteps;
  // };

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
// checks if any players have 0 health - and call the game.removePlayer(player) function on them if so
Game.prototype.checkForDeaths = function () {
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].health <= 0) {
      // removes target from active player if their target is dead - prevents healing your target back to 1 hp straight after you kill them, for example.
      if (this.players[i] === this.players[0].target) {
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
    return "Бандиты победили!";
  }
  // console.log("loops through players array:", this.players, "length:", this.players.length);
  for (var i = 0; i < this.players.length; i++) {
    // console.log("index:", i, "role:", this.players[i].role.name);
    if (this.players[i].role.name === "Шерифф") {
      // console.log("index:", i, "role found:", this.players[i].role.name);
      // console.log("sheriff found, returning null from outlaw wincheck");
      return null;
    }
  }
  // console.log("returning outlaws win because no sheriff found ??");
  return "Бандиты победили!";
}; // winConditionOutlaw [end]

Game.prototype.winCheckSheriff = function () {
  var sheriffLives = false;
  var outlawsDead = true;
  var renegadesDead = true;
  for (var i = 0; i < this.players.length; i++) {
    if (this.players[i].role.name === "Шерифф") {
      var sheriffLives = true;
    } else if (this.players[i].role.name === "Бандит") {
      outlawsDead = false;
    } else if (this.players[i].role.name === "Ренегат") {
      renegadesDead = false;
    }
  } // loop end
  if (sheriffLives && outlawsDead && renegadesDead) {
    return "Шерифф победил!";
  } else {
    return null;
  }
};

Game.prototype.winCheckRenegade = function () {
  if (this.players.length === 1 && this.players[0].role.name === "Ренегат") {
    return "Ренегат победил!";
  } else {
    return null;
  }
};

Game.prototype.winCheck = function () {
  //all win conditions checked in appropriate order

  // the if else if statement for renegade and outlaw is important, as if the sheriff is dead, the winCheckOutlaws function returns and outlaws win - this is often correct - but if a single renegade is alive, and just killed the sheriff - then the renegade wins - so we have to check if the renegade should win first, before reverting to checking if outlaws should win in the far more common case that the renegade is not the only player left alive.

  if (this.winCheckSheriff()) {
    this.wonBy = "Шерифф";
    return this.winCheckSheriff();
  }

  var outlawCheckResult = this.winCheckOutlaws();
  var renegadeCheckResult = this.winCheckRenegade();

  if (renegadeCheckResult) {
    this.wonBy = "Ренегат";
    return renegadeCheckResult;
  } else if (outlawCheckResult) {
    this.wonBy = "Бандит";
    return outlawCheckResult;
  }
  return null;
};

Game.prototype.resolveArrows = function () {
  // this.assignArrows();
  for (var i = 0; i < this.dice.arrowsRolled; i++) {
    // console.log("arrows rolled", this.dice.arrowsRolled);
    //uncomment these to test currentPlayerDead behaviour MUCH more easily (refresh til no arrows on first role with sheriff, (or else outlaws win) then roll til you get one with other players to kill them straight away)
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
  Materialize.toast("Индейцы атакуют!!", 2000);
  playSound("bow-and-arrows.mp3");
  // console.log("arrows in!");
  //adding this.checkForDeaths() call  to update who can be targetted by shots still to be resolved after arrows kill some player(s), preventing them from being targetted
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

// ridiculous one line function body (unused) - just for fun:
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
// returns true if active player can shoot their current targeted player, and false if they cannot

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
