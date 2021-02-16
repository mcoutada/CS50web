document.addEventListener("DOMContentLoaded", function () {
  // Use buttons to toggle between views
  document
    .querySelector("#inbox")
    .addEventListener("click", () => load_mailbox("inbox"));
  document
    .querySelector("#sent")
    .addEventListener("click", () => load_mailbox("sent"));
  document
    .querySelector("#archived")
    .addEventListener("click", () => load_mailbox("archive"));
  document
    .querySelector("#compose")
    .addEventListener("click", () => compose_email("", "", ""));

  // By default, load the inbox
  load_mailbox("inbox");
});

function compose_email(recipients, subject, body) {
  // Show compose view and hide other views
  document.querySelector("#compose-view").style.display = "block";
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#email-view").style.display = "none";

  // values will be empty in case of a new email call or certain in case of a reply call
  document.querySelector("#compose-recipients").value = recipients.toString();
  document.querySelector("#compose-subject").value = subject;
  document.querySelector("#compose-body").value = body;

  document.querySelector("#compose-form").onsubmit = function () {
    fetch("/emails", {
      method: "POST",
      body: JSON.stringify({
        recipients: document.querySelector("#compose-recipients").value,
        subject: document.querySelector("#compose-subject").value,
        body: document.querySelector("#compose-body").value,
      }),
    })
      // parse the data using json()
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        if (result.error) {
          alert(result.error);
        } else load_mailbox("sent");
      });
    return false;
  };
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector("#email-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "none";
  // Show the mailbox name
  document.querySelector("#emails-title").innerHTML = `<h3>${
    mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
  }</h3>`;

  fetch(`/emails/${mailbox}`)
    .then((response) => response.json())
    .then((emails) => {
      console.log(emails);
      var list = document.querySelector("#emails-list");
      list.innerHTML = "";
      console.log(emails);
      emails.forEach((element) => {
        var child = list.appendChild(document.createElement("a"));
        child.className = "list-group-item list-group-item-action";
        child.innerHTML = `<div class="d-flex justify-content-between">
                               <span>${
                                 mailbox != "sent"
                                   ? element.sender
                                   : element.recipients.toString()
                               }</span>
                               <span>${element.subject}</span>
                               <span>${element.timestamp}</span>
                          </div>`;

        if (element.read)
          child.className =
            "list-group-item list-group-item-action list-group-item-info font-weight-light font-italic";
        else
          child.className =
            "list-group-item list-group-item-action font-weight-bold";
        if (mailbox != "sent") showArchiveBtn = true;
        else showArchiveBtn = false;

        child.onclick = function () {
          return view_email(element.id, showArchiveBtn);
        };
      });
      return false;
    });
}

function view_email(emailId, showArchiveBtn) {
  document.querySelector("#email-view").style.display = "block";
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "none";
  fetch(`emails/${emailId}`)
    .then((response) => response.json())
    .then((email) => {
      console.log(email);

      document.querySelector("#email-from").value = email.sender;
      document.querySelector("#email-to").value = email.recipients.toString();
      document.querySelector("#email-subject").value = email.subject;
      document.querySelector("#email-body").value = email.body;

      document.querySelector(
        "#email-date"
      ).innerHTML = `<span>Sent on ${email.timestamp}</span><br>`;
      fetch(`/emails/${emailId}`, {
        method: "PUT",
        body: JSON.stringify({
          read: true,
        }),
      });
    });
  let ArchiveBtn = document.querySelector("#archive-button");
  if (showArchiveBtn) {
    fetch(`emails/${emailId}`)
      .then((response) => response.json())
      .then((email) => {
        ArchiveBtn.style.display = "";
        ArchiveBtn.innerHTML = email.archived ? "Unarchive" : "Archive";
        ArchiveBtn.onclick = function () {
          fetch(`/emails/${emailId}`, {
            method: "PUT",
            body: JSON.stringify({
              archived: !email.archived,
            }),
          });
          load_mailbox("inbox");
          location.reload();
          return false;
        };
      });
  } else {
    ArchiveBtn.style.display = "none";
  }
  document.querySelector("#reply-button").onclick = function () {
    fetch(`emails/${emailId}`)
      .then((response) => response.json())
      .then((email) => {
        if (email.subject.indexOf("Re: ") === -1)
          email.subject = "Re: " + email.subject;
        compose_email(
          email.sender,
          email.subject,
          "\n\n\nOn " +
            email.timestamp +
            " " +
            email.sender +
            " wrote:\n" +
            email.body
        );
      });
    return false;
  };
}
