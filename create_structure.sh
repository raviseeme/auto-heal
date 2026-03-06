#!/bin/bash

# Create directories
mkdir -p docs

mkdir -p infrastructure/bicep/modules
mkdir -p infrastructure/scripts

mkdir -p shared/contracts
mkdir -p shared/models
mkdir -p shared/utils

mkdir -p services/event-normalizer
mkdir -p services/orchestrator-core/orchestrators
mkdir -p services/orchestrator-core/activities
mkdir -p services/orchestrator-core/entities

mkdir -p services/policy-engine/app
mkdir -p services/approval-service/logicapp-definition
mkdir -p services/approval-service/templates
mkdir -p services/incident-recorder/app

mkdir -p services/execution-workers/restart-service
mkdir -p services/execution-workers/restart-agent
mkdir -p services/execution-workers/cleanup-disk

mkdir -p services/ai-advisor/app

mkdir -p catalog/policies
mkdir -p catalog/runbooks

mkdir -p database/schema
mkdir -p database/seed

mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/sample-events

mkdir -p pipelines/azure-devops
mkdir -p pipelines/github-actions

# Create files
touch README.md
touch .gitignore

touch docs/01-solution-overview.md
touch docs/02-target-architecture.md
touch docs/03-phase-1-scope.md
touch docs/04-event-schema.md
touch docs/05-remediation-catalog.md
touch docs/06-runbooks-and-guardrails.md

touch infrastructure/bicep/main.bicep
touch infrastructure/bicep/modules/servicebus.bicep
touch infrastructure/bicep/modules/storage.bicep
touch infrastructure/bicep/modules/appinsights.bicep
touch infrastructure/bicep/modules/keyvault.bicep
touch infrastructure/bicep/modules/functionapp.bicep
touch infrastructure/bicep/modules/logicapp.bicep
touch infrastructure/bicep/modules/sql.bicep
touch infrastructure/bicep/main.parameters.json

touch infrastructure/scripts/deploy.ps1
touch infrastructure/scripts/deploy.sh

touch shared/contracts/canonical-event.schema.json
touch shared/contracts/remediation-request.schema.json
touch shared/contracts/remediation-result.schema.json
touch shared/contracts/approval-decision.schema.json

touch shared/models/event.py
touch shared/models/incident.py
touch shared/models/remediation.py
touch shared/models/policy.py

touch shared/utils/logging.py
touch shared/utils/correlation.py
touch shared/utils/validation.py

touch services/event-normalizer/host.json
touch services/event-normalizer/local.settings.json.example
touch services/event-normalizer/requirements.txt
touch services/event-normalizer/function_app.py

touch services/orchestrator-core/host.json
touch services/orchestrator-core/local.settings.json.example
touch services/orchestrator-core/requirements.txt
touch services/orchestrator-core/function_app.py

touch services/orchestrator-core/orchestrators/incident_orchestrator.py

touch services/orchestrator-core/activities/store_incident.py
touch services/orchestrator-core/activities/find_known_fix.py
touch services/orchestrator-core/activities/request_approval.py
touch services/orchestrator-core/activities/execute_remediation.py
touch services/orchestrator-core/activities/update_incident.py

touch services/orchestrator-core/entities/incident_state.py

touch services/policy-engine/app/main.py
touch services/policy-engine/app/rules.py
touch services/policy-engine/app/evaluator.py
touch services/policy-engine/requirements.txt
touch services/policy-engine/Dockerfile

touch services/approval-service/logicapp-definition/approval-workflow.json
touch services/approval-service/templates/teams-card.json

touch services/incident-recorder/app/main.py
touch services/incident-recorder/app/repository.py
touch services/incident-recorder/requirements.txt
touch services/incident-recorder/Dockerfile

touch services/execution-workers/restart-service/worker.py
touch services/execution-workers/restart-service/requirements.txt
touch services/execution-workers/restart-service/Dockerfile

touch services/execution-workers/restart-agent/worker.py
touch services/execution-workers/restart-agent/requirements.txt
touch services/execution-workers/restart-agent/Dockerfile

touch services/execution-workers/cleanup-disk/worker.py
touch services/execution-workers/cleanup-disk/requirements.txt
touch services/execution-workers/cleanup-disk/Dockerfile

touch services/ai-advisor/app/main.py
touch services/ai-advisor/app/prompts.py
touch services/ai-advisor/app/mapper.py
touch services/ai-advisor/requirements.txt
touch services/ai-advisor/Dockerfile

touch catalog/remediation-catalog.json
touch catalog/policies/prod-policy.json
touch catalog/policies/nonprod-policy.json
touch catalog/policies/action-risk-matrix.json

touch catalog/runbooks/restart-service.ps1
touch catalog/runbooks/restart-agent.ps1
touch catalog/runbooks/cleanup-disk.sh

touch database/schema/001_incidents.sql
touch database/schema/002_approvals.sql
touch database/schema/003_remediation_history.sql
touch database/schema/004_known_fixes.sql

touch database/seed/seed_known_fixes.sql

touch tests/unit/test_policy_engine.py
touch tests/unit/test_correlation.py
touch tests/unit/test_catalog_mapping.py

touch tests/integration/test_event_to_approval.py
touch tests/integration/test_event_to_execution.py

touch tests/sample-events/high-cpu.json
touch tests/sample-events/service-down.json
touch tests/sample-events/disk-full.json

touch pipelines/azure-devops/azure-pipelines.yml
touch pipelines/github-actions/deploy.yml

echo "✅ Structure created successfully"