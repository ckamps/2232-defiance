'use strict';
const AWS = require("aws-sdk");
AWS.config.update({region: 'us-east-1'});

const axios = require('axios');
const reCapUrl = "https://www.google.com/recaptcha/api/siteverify";

const SecretsManager = require('./common/secretsManager.js');

// This is the SNS Topic configured so you can be emailed.
const snsTopic = "arn:aws:sns:us-east-1:052490168305:defiancehome-contact";

module.exports.webhook = async (event, context, callback) => {
  console.log("Starting ContactForm Processing for website form.");
  console.log(event)

  var secretName = 'defiancehome/recaptcha-secret-key';
  var region = 'us-east-1';
  var secretString = await SecretsManager.getSecret(secretName, region);
  const secret = JSON.parse(secretString)
  var reCaptchaSecret = secret['recaptcha-secret-key'];

  let body = event.body;
  let headers = event.headers;

  // process the urlencoded body of the form submit and put it in a map structure

  let buff = Buffer.from(body, "base64");
  let eventBodyStr = buff.toString('UTF-8');
  console.log(eventBodyStr);
  let parts = eventBodyStr.split('&');
  let result = [];
  
  // grab the params
  for (let i = 0, len = parts.length; i < len; i++) {
     let kVal = parts[i].split('=');
     // replace the + space then decode
     let key = decodeURIComponent(kVal[0].replace(/\+/g, ' '));
     result[key] = decodeURIComponent(kVal[1].replace(/\+/g, ' '));
  }
  
  // Enable to inspect the params in Amazon Cloudwatch
  console.log(result);
  
  // verify the result by POSTing to google backend with secret and
  // frontend recaptcha token as payload
  let verifyResult = await axios ({
    method: 'post',
    url: reCapUrl,
    params: {
        secret: reCaptchaSecret,
        response: result["g-recaptcha-response"]
    },
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*"
    }

  });

  // Enable to see the result
  console.log(verifyResult);

  if (verifyResult.status === 200) {
    if (verifyResult.data["success"] === true) {
      let emailbody = "Contact form submitted via:" + headers.origin +
      "\n\nFrom:"+result["name"]+
      "\nEmail: "+result["email"]+
      "\nPhone: "+result["phone"]+
      "\nRequest: "+result["request"]+
      "\n\nIP: " +headers["X-Forwarded-For"]+
      "\nUser Agent: " +headers["User-Agent"];

      // Create publish parameters
      var params = {
        Message: emailbody,
        TopicArn: snsTopic
      };

      // Create promise and SNS service object
      var publishTextPromise = new AWS.SNS({apiVersion: '2010-03-31'}).publish(params).promise();

      // Handle promise's fulfilled/rejected states
      publishTextPromise.then(
      function(data) {
        console.log("Message: " + params.Message + " was sent to the topic " + params.TopicArn);
        console.log("MessageID is " + data.MessageId);
        }).catch(
          function(err) {
            console.error(err, err.stack);
          });

        // now we return a HTTP 302 together with a URL to redirect the
        // browser to success URL
        callback(null, {
        statusCode: 302,
        headers: {
          Location: headers.origin + '/contact-response/',
        }
      });
    }
  } else {
    console.log("reCaptcha check failed. Most likely SPAM.");
  }
};