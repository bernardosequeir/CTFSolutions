import React from 'react';
import { Helmet } from 'react-helmet';
import { Link } from 'gatsby';

export default function FrogDetective() {
  return (
    <>
      <Helmet>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
        <link rel="stylesheet" href="./style.css" />
        <title>Frog Detective Tribute Page</title>
      </Helmet>

      <body>
        <main id="main">
          <header id="title">
            <h1>Frog Detective</h1>
          </header>
          <div id="img-div">
            <figure>
              <img
                id="image"
                alt="a pic of the cute boi"
                src="https://frogdetective.net/images/9.png"
              />
              <figcaption id="img-caption">
                Frog Detective, ogling at a very nice meal
              </figcaption>
              <hr />
            </figure>
          </div>
          <article id="tribute-info">
            <ul>
              <li>sometime ago - The very best boi was born</li>
              <li>
                some time after - he became a detective. a great win for the
                rights of frogs
              </li>
              <li>
                even some more time after that - he became THE VERY SECOND BEST
                DETECTIVE OF THE ENTIRE WORLD
              </li>
              <li>
                years later - a very funny person called Grace Bruxner got in
                touch with him and made two games about him
              </li>
              <li>
                first game - extremely funny and cute!! also gave frog detective
                a chance to display his skills
              </li>
              <li>
                second game - idk i haven't played it yet but it looks pretty
                cool ig
              </li>
            </ul>
            <a
              id="tribute-link"
              href="https://twitter.com/frogdetective"
              target="_blank"
              rel="noopener noreferrer"
            >
              His twitter.
            </a>
          </article>
        </main>
      </body>
    </>
  );
}
