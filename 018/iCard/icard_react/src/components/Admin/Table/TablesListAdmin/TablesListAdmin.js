import React from "react";
import { Label, Button, Icon, Checkbox } from "semantic-ui-react";
import { map, size } from "lodash";
import { ReactComponent as IcTable } from "../../../../assets/table.svg";
import "./TablesListAdmin.scss";

export function TablesListAdmin(props) {
  const { tables } = props;

  return (
    <div className="tables-list-admin">
      {map(tables, (table) => (
        <h2>Mesa</h2>
      ))}
    </div>
  );
}
