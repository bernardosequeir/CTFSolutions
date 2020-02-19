/* eslint-disable react/display-name */
import React from 'react';
import { css } from '@emotion/core';
import { useStaticQuery, Link, graphql } from 'gatsby';

import { rhythm } from '../utils/typography';

export default ({ children }) => {
  const data = useStaticQuery(
    graphql`
      query {
        site {
          siteMetadata {
            title
          }
        }
      }
    `
  );
  return (
    <div
      css={css`
        margin: 0 auto;
        max-width: 50%;
        padding: ${rhythm(2)};
        padding-top: ${rhythm(1.5)};
        back
      `}
    >
      <Link to="/">
        <h3
          css={css`
            margin-bottom: ${rhythm(2)};
            display: inline-block;
            font-style: normal;
          `}
        >
          {data.site.siteMetadata.title}
        </h3>
      </Link>
      <Link
        to="/about/"
        css={css`
          float: right;
        `}
      >
        About
      </Link>
      {children}
      <div className="dark-mode-switch">
        <input
          id="dark-mode"
          type="checkbox"
          onClick="document.documentElement.classList.toggle('dark-mode')"
        ></input>
        <label htmlFor="dark-mode">Dark Mode</label>
      </div>
    </div>
  );
};
