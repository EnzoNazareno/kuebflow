from kfp import dsl
from kfp.components import load_component_from_file

@dsl.pipeline(
    name="Mental Health Chatbot Pipeline",
    description="Pipeline KFPv2 with PVC-mounted components"
)
def chatbot_pipeline():
    # Load components (already contain volume mounts in their YAMLs)
    load_dataset = load_component_from_file('../components/load_dataset/component.yaml')
    preprocess = load_component_from_file('components/data_preprocessing/component.yaml')
    train = load_component_from_file('components/train_model/component.yaml')
    evaluate = load_component_from_file('components/evaluate_model/component.yaml')
    deploy = load_component_from_file('components/deploy_model/component.yaml')

    # Step 1: Load Dataset
    load_dataset_task = load_dataset()

    # Step 2: Preprocess
    preprocess_task = preprocess()

    # Step 3: Train model
    train_task = train(
        input_data=preprocess_task.outputs['processed_data']
    )

    # Step 4: Evaluate model
    evaluate_task = evaluate(
        model=train_task.outputs['model'],
        data=preprocess_task.outputs['processed_data']
    )

    # Step 5: Deploy model
    deploy_task = deploy(
        model=train_task.outputs['model']
    )
