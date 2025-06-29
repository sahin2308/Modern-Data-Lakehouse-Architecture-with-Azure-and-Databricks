{
  "name": "End to End Pipeline",
  "email_notifications": {
    "no_alert_for_skipped_runs": false
  },
  "webhook_notifications": {},
  "timeout_seconds": 0,
  "max_concurrent_runs": 1,
  "tasks": [
    {
      "task_key": "Reading_Parameter",
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Parameter",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Bronze_AutoLoader_Iteration",
      "depends_on": [
        {
          "task_key": "Reading_Parameter"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "for_each_task": {
        "inputs": "{{tasks.Reading_Parameter.values.input_datasets}}",
        "task": {
          "task_key": "Bronze_AutoLoader_Iteration_iteration",
          "run_if": "ALL_SUCCESS",
          "notebook_task": {
            "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Bronze_Layer",
            "base_parameters": {
              "p_folder_name": "{{input.p_folder_name}}"
            },
            "source": "WORKSPACE"
          },
          "timeout_seconds": 0,
          "email_notifications": {},
          "webhook_notifications": {}
        }
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Silver_Customers",
      "depends_on": [
        {
          "task_key": "Bronze_AutoLoader_Iteration"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Silver_Customers",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Silver_Orders",
      "depends_on": [
        {
          "task_key": "Bronze_AutoLoader_Iteration"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Silver_Orders",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Silver_Products",
      "depends_on": [
        {
          "task_key": "Bronze_AutoLoader_Iteration"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Silver_Products",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Gold_Customers",
      "depends_on": [
        {
          "task_key": "Silver_Products"
        },
        {
          "task_key": "Silver_Orders"
        },
        {
          "task_key": "Silver_Customers"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Gold_Customers",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Gold_Prodcuts",
      "depends_on": [
        {
          "task_key": "Silver_Orders"
        },
        {
          "task_key": "Silver_Customers"
        },
        {
          "task_key": "Silver_Products"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "pipeline_task": {
        "pipeline_id": "a362e72a-aaa0-4592-999f-60d6ae56a9c4",
        "full_refresh": false
      },
      "timeout_seconds": 0,
      "email_notifications": {},
      "webhook_notifications": {}
    },
    {
      "task_key": "Gold_Orders",
      "depends_on": [
        {
          "task_key": "Gold_Prodcuts"
        },
        {
          "task_key": "Gold_Customers"
        }
      ],
      "run_if": "ALL_SUCCESS",
      "notebook_task": {
        "notebook_path": "/Workspace/Users/chotusaikh253@gmail.com/Databricks ETE Project/Gold_Orders",
        "source": "WORKSPACE"
      },
      "timeout_seconds": 0,
      "email_notifications": {}
    }
  ],
  "queue": {
    "enabled": true
  },
  "performance_target": "STANDARD",
  "run_as": {
    "user_name": "chotusaikh253@gmail.com"
  }
}