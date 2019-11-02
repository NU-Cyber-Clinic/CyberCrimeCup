const Discord = require('discord.js');
const client = new Discord.Client();

const ytdl = require("ytdl-core");
const opus = require('opusscript');
const request = require("request");
const cheerio = require('cheerio');
const fs = require('fs');

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);

  checkChallengeCount();
  setInterval(function () {
    checkChallengeCount();
  }, 60 * 1000);
});

function checkChallengeCount() {

  var options = {
    method: 'GET',
    url: 'https://www.cybercrime.co.uk/dashboard-challenges',
    headers: {
      "Cookie": "PHPSESSID=CHANGE_ME"
    }
  };

  request(options, function (error, response, body) {
    if (error) throw new Error(error);

    var doc = cheerio.load(body);
    var chal_count = doc(".col-lg-5 .btn.btn-block").length;

    var chal_count_last = parseInt(fs.readFileSync("chal_count.txt", {
      encoding: "utf-8"
    }));

    if (chal_count > chal_count_last) {
      fs.writeFile("chal_count.txt", chal_count, () => {})
      panic(chal_count);
    }
  });
}

function panic(chal_count) {
  client.channels.get("517388963665805334").send("New challenge! https://www.cybercrime.co.uk/dashboard-challenge-preview/10" + chal_count + " <@170429173003714560> <@505414674003656765> <@220548182650781696> <@215715196960768002> <@545297878172827659>");

  const streamOptions = {
    seek: 0,
    volume: 1
  };

  client.channels.get("517389057102184462").join().then(connection => {
    console.log("joined channel");
    const stream = ytdl('https://www.youtube.com/watch?v=dQw4w9WgXcQ', {
      filter: 'audioonly'
    });
    const dispatcher = connection.playStream(stream, streamOptions);
    dispatcher.on("end", end => {
      console.log("left channel");
      voiceChannel.leave();
    });
  }).catch(err => console.log(err));
}

//https://discordapp.com/oauth2/authorize?&client_id=639969001954607134&scope=bot&permissions=0
client.login('NjM5OTY5MDAxOTU0NjA3MTM0.Xby_og.xCjT9tCeYgbc2fGcjUkl5QCdz_w');