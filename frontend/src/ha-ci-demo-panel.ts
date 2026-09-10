import { LitElement, css, html } from "lit";
import { customElement, property } from "lit/decorators.js";

/** The smallest panel that still exercises the whole frontend path. */
@customElement("ha-ci-demo-panel")
export class HaCiDemoPanel extends LitElement {
  @property({ attribute: false }) public narrow = false;

  static override styles = css`
    :host {
      display: block;
      padding: 16px;
      color: var(--primary-text-color);
    }
  `;

  protected override render() {
    return html`<p>${this.narrow ? "narrow" : "wide"}</p>`;
  }
}

/** The label the panel shows for a width, kept pure so a test can reach it. */
export function widthLabel(narrow: boolean): string {
  return narrow ? "narrow" : "wide";
}
