# CLI Features and usage

Running the CLI can be done by executing:

```
cd imdb-data/
docker compose run --rm imdb_cli
```

Once it checks that the containers it depends on are running, it will execute. It will welcome the user and show any warnings if they exist.

<img width="1041" height="119" alt="imagen" src="https://github.com/user-attachments/assets/82bce777-c5d5-4166-adfc-2bd66d538f00" />

## Commands
Using `help`, will return a list of the available commands.

<img width="1429" height="131" alt="imagen" src="https://github.com/user-attachments/assets/f863c08f-b4c7-4fe6-a295-4474ad8b7ff3" />

### Get person information

Using `person <role> <name {surname(s)}>` will return relevant information on the searched person. It is important to specify the role the person plays as it will lead to more precise responses. Refer to the IMDb dataset documentation to check more on this.

*Examples:*

<img width="1504" height="69" alt="imagen" src="https://github.com/user-attachments/assets/8313d042-a1ec-4a38-8446-67f4ed8503c9" />

<img width="1504" height="69" alt="imagen" src="https://github.com/user-attachments/assets/cf9f56e6-3eb5-4584-a6e2-16cfa313545e" />

*Misses on the data and errors are shown in a comprehensible format*
<img width="713" height="69" alt="imagen" src="https://github.com/user-attachments/assets/b7002116-1ca7-4ce4-bde0-dc15424f0be2" />

### Get title information
Using `title <kind> <name>` will return relevant information on the searched title. It is important to specify the kind of title to get more precise responses. Refer to the IMDb dataset documentation to check more on this.
In this case, it will return basic title information together with the title's rating and some of the principals that take part in them.

*Examples:*
<img width="1226" height="82" alt="imagen" src="https://github.com/user-attachments/assets/40777066-2a20-4d74-b94e-e76fd702dd6a" />

<img width="1226" height="82" alt="imagen" src="https://github.com/user-attachments/assets/8284f719-1fb0-43cb-a64b-a9a702546f9a" />

<img width="1300" height="82" alt="imagen" src="https://github.com/user-attachments/assets/32dc544a-3e01-45d9-93c9-4f0fa75af8d8" />

## Styling and user experience

The CLI offers a friendly interface for the user to query the database. The CLI application main colors are chosen to be similar to the main IMDb color palette. *However, depending on the used terminal, colors and font weight might display different.*
